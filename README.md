# Python编程快速上手，让繁琐工作自动化
## 第 1 章 Python 基础

*做过的事比仅仅读过的内容，更令人印象深刻。*   
在 Ubuntu 上，打开新的终端窗口并输入 idle3 启动 IDLE 交互式环境。
```python
>>> 'Alice' + 'bob'  # 字符串连接
'Alicebob'
>>> 'Alice' * 5    # * 用于两个整型或浮点型值时表示乘法，用于字符串和整型值时表示“字符串复制”
'AliceAliceAliceAliceAlice'
```
**变量名需符合以下3个规则：**
1. 只能包含一个词。
2. 只能包含字母、数字和下划线。
3. 不能以数字开头。  
  变量用小写字母开头是 Python 的管理。
```python
print ('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

print()  # 打印一个空行
input()  # 等待用户在键盘上输入一些文本，并按下回车键。
len()    # 字符串中字符的个数
str()
int()
float()
//  # 取商
**  # 幂

```

## 第 2 章 控制流
所有控制流语句都以冒号结尾。  
git 提交报错：Can't update: no tracked branch  
解决方法：VCS>Git>Rebase    
**range(5, -1, -1)** 开始值，结束值（不包括），步长  
用 **sys.exit()** 提前结束程序    
###### round()
###### abs()    
```python
>>> abs(4+3j)       # 返回实数的绝对值，复数的模  |z|= √a²+b² a的平方加b的平方的平方根。
5.0
>>> round(0.5)      # Python3 会把 x 四舍五入为最近的偶数倍数，出现*.5的情况下，用的不是四舍五入，是运算更靠近偶数的整数。
0
>>> round(0.6)
1
>>> round(1.5)
2
>>> round(-1.5)
-2
>>> round(-0.5)
0
>>> round(0.567)
1
```
## 第 3 章 函数
记住，表达式是值和操作符的组合。
None 必须大写首字母 N，表示没有值。
```python
>>> spam = print('Hello!')
Hello!
>>> None == spam    # 在幕后，对于所有没有 return 语句的函数定义，Python 都会在末尾加上 return None
True
>>> print('Hello','world',sep=',')
Hello,world

print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
Print objects to the text stream file, separated by sep and followed by end. sep, end and file, if present, must be given as keyword arguments.
```
  有 4 条法则，来区分一个变量是处于局部作用还是全局作用域：
1. 如果变量在全局作用域中使用（即在所有函数之外），它就总是全局变量。
2. 如果在一个函数中，有针对该变量的 global 语句，它就是全局变量。
3. 否则，如果该变量用于函数中的赋值语句，它就是局部变量。
4. 但是，如果该变量没有用在赋值语句中，它就是全局变量。

