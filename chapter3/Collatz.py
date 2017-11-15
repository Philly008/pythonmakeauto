# coding=UTF-8
# 从用户读入一个值，并判断这个值是不是一个int类型的整数，如果不是给出异常提示
# 如果这个值是偶数 那么让这个数//2
# 如果这个值是奇数 那么让这个数 ×3 + 1
# 通过不断调用函数的返回值 并打印这个返回值 直到这个返回值为1

num = input("please input a number: ")
#except NameError:
#   print ("Your input is not a number")

def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return num * 3 + 1
    return num

isnumber = 1
try:
    num = int(num)
except ValueError:
    print ("Your input is not a nubmer")
    isnumber = 0
while num != 1:
    if isnumber == 1:
        num = collatz(num)
        print (num)
    else:
        break