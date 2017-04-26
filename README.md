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

## 第 4 章 列表
```python
>>> spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
>>> spam[0]
['cat', 'bat']
>>> spam[0][1]      # 下标只能是整数，不能是浮点数。列表中第一个值的下标是 0
'bat'
>>> spam = [10, 20, 30, 40, 50]
>>> spam
[10, 20, 30, 40, 50]
>>> del spam[2]     # 删除列表中下标处的值
>>> spam
[10, 20, 40, 50]

>>> cat = ['fat', 'black', 'loud']
>>> size, color, disposition = cat  # 多重赋值。变量的数目和列表的长度必须严格相等。


>>> type(('hello',))    # 元组中只有一个值，可以在括号内该值的后面加上一个逗号。
<class 'tuple'>
>>> type(('hello'))
<class 'str'>

>>> spam = [0, 1, 2, 3, 4, 5]
>>> cheese = spam
>>> cheese[1] = 'Hello!'
>>> spam        # 引用指向同一个列表
[0, 'Hello!', 2, 3, 4, 5]
>>> cheese
[0, 'Hello!', 2, 3, 4, 5]
```
**spam[2] 是一个列表和下标。**        
**spam[1:4] 是一个列表和切片。切片向上增长，但不包括第二个下标的值。**        
    一个常见的 Python 技巧，是在 for 循环中使用 range(len(someList)), 迭代列表的每一个下标。    
    用 index() 方法在列表中查找值    
    用 append() 和 insert() 方法在列表中添加值。    
    用 remove() 方法从列表中删除值    
    用 sort() 方法将列表中的值排序    
    在行末使用续行字符 \ ，将一条指令写成多行。    
    元组与列表的主要区别在于，元组像字符串一样，是不可变的。    
    用 list() 和 tuple() 函数来转换类型。    
    变量包含对列表值得引用，而不是列表值本身。但对于字符串和整数值就包含了字符串或整数值。    
    **copy()**:用来复制列表或字典这样的可变值，而不只是复制引用        
    **deepcopy()**：如果要复制的列表中包含了列表，就用此方法。        
 
## 第 5 章 字典和结构化数据
    keys()
    values()
    items()
    in
    not in
    get()
    setdefault()
    
```python
>>> spam = {'color':'red', 'age':42}
>>> spam.keys()
dict_keys(['color', 'age'])
>>> list(spam.keys())
['color', 'age']
>>> for k, v in spam.items():
	print('Key: ' + k + ' Value: ' + str(v))

	
Key: color Value: red
Key: age Value: 42
```
    如果程序中导入 pprint 模块，就可以使用 pprint() 和 pformat() 函数，它们将“漂亮打印”一个字典的字。
    'cat' in spam 检查字典中是不是有一个 'cat' 键，而 'cat' in spam.values() 检查是否有一个值 'cat' 对应于 spam 中的某个键。
    
## 第 6 章 字符串操作
使用双引号的一个好处就是字符串中可以使用单引号字符。
**转义字符：**
\'  单引号
\"  双引号
\t  制表符
\n  换行符
\\  倒斜杠
可以在字符串开始的引号之前加上 r ，使它成为原始字符串，忽略所有的转义字符。
用三重引号的多行字符串
多行注释：""" """
**有用的字符串方法：**
upper()
lower()
isupper()
islower()
isalpha() 返回 True，如果字符串只包含字母，并且非空；
isalnum() 返回 True，如果字符串只包含字母和数字，并且非空；
isdecimal() 返回 True，如果字符串只包含数字字符，并且非空；
isspace() 返回 True，如果只包含空格、制表符和换行，并且非空；
istitle() 返回 True，如果字符串仅包含大写字母开头、后面都是小写字母的单词。
startswith()
endswith()
```python
>>> 'abc12345'.islower()
True
>>> '12345'.islower()
False
>>> ', '.join(['cats', 'rats', 'hats'])
'cats, rats, hats'
>>> 'cats, rats, hats'.split(', ')
['cats', 'rats', 'hats']
>>> 'Hello'.rjust(20, '*')
'***************Hello'
>>> spam = 'SpamSpamBaconSpamEggsSpamSpam'
>>> spam.strip('ampS')  # 告诉它在变量中存储的字符串两端，删除出现的 a、m、p和大写的 S。
'BaconSpamEggs'
```
join()  调用join() 方法的字符串，被插入到列表参数中每个字符串的中间。
split()
rjust()  右对齐
ljust()
center()
strip()     删除空白字符
rstrip()
lstrip()
**用 pyperclip 模块拷贝粘贴字符串：copy(), paste()**
安装第三方模块：
pip install ModuleName
pip install -U ModuleName   // 升级到最新版本
```python
>>> import pyperclip
>>> pyperclip.copy('Hello world!')
>>> pyperclip.paste()
'Hello world!'
```