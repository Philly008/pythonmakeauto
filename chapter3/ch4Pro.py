#!/usr/bin/env python3.5
# coding:utf-8
# 假定有一个列表，编写函数以一个列表值作为参数，返回一个字条串
# 该字符串包含所有表项，之间以逗号和空格分隔，并在最后一个值前插入 and
# 要求函数能处理传递给它的任何列表

# spam = input('please input a list:')
# 刚开始想从用户输入进行传递列表方式，但没成功

# 4.10.1
print("4.10.1 answer:")
def chlist_str(spam):
    spam[-1] = 'and ' + spam[-1]
    str_list = ', '.join(spam)
    return str_list
new_str = chlist_str(['apple','banana','tofu','cats'])
print("convert str is:")
print(new_str)

# 4.10.2
# 这道题的目的在于进行嵌套列表的行列转换吧
print("4.10.2 answer:")
grid = [['.','.','.','.','.','.'],
          ['.','o','o','.','.','.'],
          ['o','o','o','o','.','.'],
          ['o','o','o','o','o','.'],
          ['.','o','o','o','o','o'],
          ['o','o','o','o','o','.'],
          ['o','o','o','o','.','.'],
          ['.','o','o','.','.','.'],
          ['.','.','.','.','.','.']]

# 第一种实现方法，因为这个列表的行列长度不相等，外层循环的换行数应该是子列表的长度。
for row in range(0,len(grid[0])):
    for col in range(0,len(grid)):
#       print(''.join(grid[col][row]),end='')
        print(grid[col][row],end='')
    print()

# 第二种实现方法，
for row in zip(*grid):
    for col in row:
#        print(''.join(col),end='')
         print(col,end='')
    print()