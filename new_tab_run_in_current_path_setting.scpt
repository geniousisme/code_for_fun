(*
This script opens a new Terminal.app tab in the directory of the current tab with the same settings. You’ll need to, if you haven’t already, enable access for assistive devices as described here: http://www.macosxautomation.com/applescript/uiscripting/index.html

It’s almost all the work of two scripts put together, thank you to them:

Chris Johnsen’s script opens a new tab in the current directory: http://superuser.com/questions/61149/os-x-terminal-app-how-to-start-a-new-tab-in-the-same-directory-as-the-current-ta/61264#61264

Jacob Rus’s “menu_click” lets me create the tab with the same settings, as Terminal’s API doesn’t: http://hints.macworld.com/article.php?story=20060921045743404

If you change the name of a Terminal profile, the AppleScript API returns the old name until you restart the application, so the script won’t work on renamed settings until then. Ugh. Also, the necessity of activating Terminal to execute the menu command brings all the terminal windows to the front.
*)

-- from http://hints.macworld.com/article.php?story=20060921045743404
-- `menu_click`, by Jacob Rus, September 2006
-- 
-- Accepts a list of form: `{"Finder", "View", "Arrange By", "Date"}`
-- Execute the specified menu item.  In this case, assuming the Finder 
-- is the active application, arranging the frontmost folder by date.

on menu_click(mList)
	local appName, topMenu, r
	
	-- Validate our input
	if mList's length < 3 then error "Menu list is not long enough"
	
	-- Set these variables for clarity and brevity later on
	set {appName, topMenu} to (items 1 through 2 of mList)
	set r to (items 3 through (mList's length) of mList)
	
	-- This overly-long line calls the menu_recurse function with
	-- two arguments: r, and a reference to the top-level menu
	tell application "System Events" to my menu_click_recurse(r, ((process appName)'s ¬
		(menu bar 1)'s (menu bar item topMenu)'s (menu topMenu)))
end menu_click

on menu_click_recurse(mList, parentObject)
	local f, r
	
	-- `f` = first item, `r` = rest of items
	set f to item 1 of mList
	if mList's length > 1 then set r to (items 2 through (mList's length) of mList)
	
	-- either actually click the menu item, or recurse again
	tell application "System Events"
		if mList's length is 1 then
			click parentObject's menu item f
		else
			my menu_click_recurse(r, (parentObject's (menu item f)'s (menu f)))
		end if
	end tell
end menu_click_recurse



-- with the noted slight modification, from http://superuser.com/questions/61149/os-x-terminal-app-how-to-start-a-new-tab-in-the-same-directory-as-the-current-ta/61264#61264

on run
	(* Find the tty. *)
	-- This is ugly. But is seems to work on Tiger. Maybe newer releases can do better.
	tell application "Terminal"
		set w to the front window
		tell w
			set origName to name
			set title displays device name to not title displays device name
			set newName to name
			set title displays device name to not title displays device name
		end tell
	end tell
	set tty to extractTTY(origName, newName)
	if tty is "" then
		display dialog "Could not find the tty for of the current Terminal window." buttons "Cancel" cancel button "Cancel" default button "Cancel"
	end if
	
	(* Find the PIDs of the processes in the foreground process group on that tty. *)
	set pids to paragraphs of (do shell script "
ps -o pid,tty,tpgid,pgid,state,command |
awk '
    BEGIN   {t=ARGV[1];ARGC=1}
    $2==t && $3==$4 {print $1}
' " & quoted form of tty)
	if pids is {} or pids is {""} then
		display dialog "Could not find the processes for " & tty & "." buttons "Cancel" cancel button "Cancel" default button "Cancel"
	end if
	
	(* Find the unique cwds of those processes. *)
	set text item delimiters to {","}
	set lsof to do shell script "lsof -F 0n -a -d cwd -p " & quoted form of (pids as Unicode text) without altering line endings
	set text item delimiters to {(ASCII character 0) & (ASCII character 10)}
	set cwds to {}
	repeat with lsofItem in text items of lsof
		if lsofItem starts with "n" then
			set cwd to text 2 through end of lsofItem
			if cwds does not contain cwd then ¬
				set end of cwds to cwd
		end if
	end repeat
	if cwds is {} then
		display dialog "No cwds found!?" buttons "Cancel" cancel button "Cancel" default button "Cancel"
	end if
	if length of cwds is greater than 1 then
		set cwds to choose from list cwds with title "Multiple Distinct CWDs" with prompt "Choose the directory to use:" without multiple selections allowed and empty selection allowed
		if cwds is false then error number -128 -- cancel
	end if
	
	(* Open a new Terminal. *)
	
	-- Here is where I substituted the menu_click call to use the current settings
	
	tell application "Terminal"
		activate
		tell window 1
			set settings to name of current settings in selected tab
		end tell
	end tell
	menu_click({"Terminal", "Shell", "New Tab", settings})
	
	tell application "Terminal" to do script "cd " & quoted form of item 1 of cwds in selected tab of window 1
end run

to extractTTY(a, b)
	set str to textLeftAfterRemovingMatchingHeadAndTail(a, b)
	set offs to offset of "tty" in str
	if offs > 0 then
		return text offs through (offs + 6) of str
	end if
	return ""
end extractTTY
to textLeftAfterRemovingMatchingHeadAndTail(big, little)
	set text item delimiters to space
	if class of big is not list then set big to text items of big
	if class of little is not list then set little to text items of little
	set {maxLen, minLen} to {length of big, length of little}
	if maxLen < minLen then ¬
		set {big, little, maxLen, minLen} to {little, big, minLen, maxLen}
	
	set start to missing value
	repeat with i from 1 to minLen
		if item i of big is not equal to item i of little then
			set start to i
			exit repeat
		end if
	end repeat
	if start is missing value then
		if maxLen is equal to minLen then
			return ""
		else
			return items (minLen + 1) through end of big as Unicode text
		end if
	end if
	
	set finish to missing value
	repeat with i from -1 to -minLen by -1
		if item i of big is not equal to item i of little then
			set finish to i
			exit repeat
		end if
	end repeat
	if finish is missing value then set finish to -(minLen + 1)
	
	return items start through finish of big as Unicode text
end textLeftAfterRemovingMatchingHeadAndTail