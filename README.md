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

