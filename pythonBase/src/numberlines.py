import fileinput                         #  1
for line in fileinput.input(inplace=1):  #  2
    line = line.rstrip()                 #  3
    num = fileinput.lineno()             #  4
    print('%-40s # %2i' % (line, num))   #  5
