import sys
'''
How to use this program?
python duplicateStats.py file_name
ex. python duplicateStats.py VJ0012.txt
'''
def duplicate_stats(file_name):
    input_file = open(file_name, 'r')
    lines      = input_file.readlines()
    line_num   = len(lines)
    line_dict  = {}
    
    for i in xrange(line_num):
        if i % 2 == 0:
           line_dict[lines[i][:-1]] = line_dict.get(lines[i][:-1], 0) + 1

    for key, val in line_dict.items():
        print key, ':', val

if __name__ == '__main__':
   
   file_name = sys.argv[1]
   duplicate_stats(file_name)

  

