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
```


