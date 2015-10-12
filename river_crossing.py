""""
([left side][right side])
inital state: ([Farmer, Fox, Chicken, Grain] [])
move 1: ([Chicken, Grain] [Farmer, Fox]) "unsafe"
move 2: ([Fox, Grain] [Farmer, Chicken]) "safe"
move 3: ([Fox, Chicken] [Farmer, Grain]) "unsafe"
move 4: ([Fox, Chicken, Grain] [Farmer]) "unsafe"

([Fox, Grain] [Farmer, Chicken])
([Farmer, Fox, Grain] [Chicken]) "safe"
([Farmer, Fox, Chicken, Grain] []) "safe"

Take chicken over (right)
Return (left)
Take fox over (right)
Return with chicken (left) <--
Take grain over (right)
Return (left)
Take chicken over (right)
"""

class Solution(object):
    def __init__(self):
        self.left  = [1, 1, 1, 1]
        self.right = [0, 0, 0, 0]
        self.states = [[list(self.left), list(self.right)]]
        self.idx_hash = {"Farmer": 0, "Fox": 1, "Chicken": 2, "Grain": 3}

    def move_generator(self):
        print "from left to right"
        self.move_gen_helper(self.left, self.right, "left2right")
        print "from right to left"
        self.move_gen_helper(self.right, self.left, "right2left")

    def move_gen_helper(self, move_from, move_to, direction):
        print "left:",  self.left
        print "right:", self.right
        for i in xrange(4):
            if move_from[i]:
                move_from[i] = 0
                move_from[self.idx_hash["Farmer"]] = 0
                if self.is_river_safe(move_from):
                    move_to[i] = 1
                    move_to[self.idx_hash["Farmer"]] = 1
                    if direction == "left2right":
                        if not self.is_state_repeated(move_from, move_to):
                            self.save_state(move_from, move_to)
                            break
                    elif direction == "right2left":
                        if not self.is_state_repeated(move_to, move_from):
                            self.save_state(move_to, move_from)
                            break
                move_to[i] = 0
                move_from[i] = 1
        self.left, self.right =                                                \
                              list(self.states[-1][0]), list(self.states[-1][1])

    def save_state(self, left, right):
        new_state = [list(left), list(right)]
        self.states.append(new_state)

    def is_state_repeated(self, left, right):
        return [left, right] in self.states

    def is_river_safe(self, river_side):
        if river_side[self.idx_hash["Fox"]] and                                \
           river_side[self.idx_hash["Chicken"]]:
            return False
        elif river_side[self.idx_hash["Chicken"]] and                          \
             river_side[self.idx_hash["Grain"]]:
            return False
        else:
            return True

    def is_all_on_right_side(self):
        return sum(self.right) == 4

    def river_crossing(self):
        while not self.is_all_on_right_side():
            self.move_generator()
        print "yeah, finish!!"

if __name__ == "__main__":
    s = Solution()
    s.river_crossing()