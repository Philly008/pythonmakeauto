
'''
Created on 2016年12月15日

@author: admin

print('hola')

result = [1, 2, 3]
for x in range(3):
    for y in range(3):
        result.append((x, y))

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print([b+'+'+g for b in boys for g in letterGirls[b[0]]])

if name == 'Ralph Auldus Melish':
    print('welcome!')
elif name == 'Enid':
    # 还没完。。。
    pass
elif name == 'Bill Gates':
    print('Access Denied')

from math import sqrt
scope = {}
exec ('sqrt = 1' , scope)
sqrt(4)

fibs = [0, 1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)

fibs = [0, 1]
num = int(input('How many Fibonacci numbers do you want? '))
for i in range(num - 2):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)

def hello(name):
    return 'Hello, ' + name + '!'
print(hello('world'))
print(hello('Gumby'))

def fibs(num):
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result
print(fibs(15))


def square(x):
    'Calculates the square of the number x.'
    return x*x 
print(square.__doc__)

help(square)

def test():
    print('This is printed')
    return
    print('This is not')
x = test()
x
print(x)

# begin
storage = {}
storage['first'] = {}
storage['middle'] = {}
storage['last'] = {}

me = 'Magnus Lie Hetland'
storage['first']['Magnus'] = [me]
storage['middle']['Lie'] = [me]
storage['last']['Hetland'] = [me]
print (storage['middle']['Lie'])

my_sister = 'Anne Lie Hetland'
storage['first'].setdefault('Anne', []).append(my_sister)
storage['middle'].setdefault('Lie', []).append(my_sister)
storage['last'].setdefault('Hetland', []).append(my_sister)
print(storage['first']['Anne'])
print(storage['middle']['Lie'])

def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}
    
storage = {}
init(storage)
#print(storage)
 
    
def lookup(data, label, name):
    return data[label].get(name)
#print(lookup(storage, 'middle', 'Lie'))

def store(data, full_name):
    names = full_name.split()
    if len(names) == 2: names.insert(1, '')
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
                data[label][name] = [full_name]

MyNames = {}
init(MyNames)
store(MyNames, 'Magnus Lie Hetland')
print(lookup(MyNames, 'middle', 'Lie'))
store(MyNames, 'Robin Hood')
store(MyNames, 'Robin Locksley')
print(lookup(MyNames, 'first', 'Robin'))
store(MyNames, 'Mr. Gumby')
print(lookup(MyNames, 'middle', ''))
# end


def inc(x): x[0] = x[0] + 1
foo = [10]
inc(foo)
print(foo)


def hello_1(greeting, name):
    print('%s, %s!' % (greeting, name))
def hello_2(name, greeting):
    print ('%s, %s!' % (name, greeting))
hello_1('Hello', 'world')
hello_2('Hello', 'world')
hello_1(greeting='Hello', name='world')
hello_1(name='world', greeting='Hello')
hello_2(greeting='Hello', name='world')         # 参数名和值一定要对应

def hello_3(greeting='Hello', name='world'):
    print('%s, %s!' % (greeting, name))
   
hello_3()
hello_3('Greetings')
hello_3('Greetings', 'universe')
hello_3(name='Gumby')
def hello_4(name, greeting='Hello', punctuation='!'):
    print('%s, %s%s' % (greeting, name, punctuation))
hello_4('Mars')
hello_4('Mars', 'Howdy')
hello_4('Mars', 'Howdy', '...')
hello_4('Mars', punctuation='.')
hello_4('Mars', greeting='Top of the morning to ya')
hello_4()


def print_params(*params):
    print(params)
print_params('Testing')
print_params(1, 2, 3)
def print_params_2(title, *params):
    print(title)
    print(params)
print_params_2('Params: ', 1, 2, 3)
print_params_2('Nothing: ')
#print_params_2('Hmm...', something=42)
def print_params_3(**params):       # 两个星号能够处理关键字参数的“收集”，返回的是字典
    print(params)
print_params_3(x=1, y=2, z=3)
def print_params_4(x, y, z=3, *pospar, **keypar):
    print(x, y, z)
    print(pospar)
    print(keypar)
print_params_4(1, 2, 3, 5, 6, 7, foo=1, bar=2)
print_params_4(1, 2)


def add(x, y): return x + y 
params = (1, 2)
print(add(*params))
params = {'name': 'Sir Robin', 'greeting': 'Well met'}
hello_3(**params)


def with_stars(**kwds):
    print(kwds['name'], 'is', kwds['age'], 'years old')
def without_stars(kwds):
    print(kwds['name'], 'is', kwds['age'], 'years old')
args = {'name': 'Mr. Gumby', 'age': 42}
with_stars(**args)
without_stars(args)

def foo(x, y, z, m=0, n=0):
    print(x, y, z, m, n)
def call_foo(*args, **kwds):
    print("Calling foo!")
    foo(*args, **kwds)


def story(**kwds):
    return 'Once upon a time, there was a ' \
        '%(job)s called %(name)s.' % kwds
def power(x, y, *others):
    if others:
        print('Received redundant parameters: ', others)
    return pow(x, y)
def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop is None:    # 如果没有为 stop 提供值
        start, stop=0, start    # 指定参数
    result = []
    i = start       # 计算 Start 索引
    while i < stop:     # 直到计算到 stop 的索引
        result.append(i)        # 将索引添加到 result 内
        i += step           # 用 step(>0) 增加索引
    return result
print(story(job='king', name='Gumby'))
print(story(name='Sir Robin', job='brave knight'))
params = {'job': 'language', 'name':'Python'}
print(story(**params))
del params['job']
print(story(job='stroke of genius', **params))
print(power(2, 3))
print(power(3, 2))
print(power(y=3, x=2))
params = (5,) * 2
print(power(*params))
print(power(3, 3, 'Hello, world'))
print(interval(10))
print(interval(1, 5))
print(interval(3, 12, 4))
print(power(*interval(3, 7)))


def foo():
    def bar():
        print("Hello, world!")
    bar()


def multiplier(factor):
    def multiplyByFactor(number):
        return number * factor 
    return multiplyByFactor
double = multiplier(2)
print(double(5))
triple = multiplier(3)
print(triple(3))
print(multiplier(5)(4))


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)


def search(sequence, number, lower=0, upper=None):
    if upper is None: upper = len(sequence)-1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle+1, upper)
        else:
            return search(sequence, number, lower, middle)
seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
print(seq)
print(search(seq, 34))
print(search(seq, 100))


from random import choice
x = choice(['Hello, world!', [1, 2, 'e', 'e', 4]])
print(x.count('e'))


def add(x, y):
    return x+y 
print(add(1, 2))
print(add('Fish', 'license'))

def length_message(x):
    print("The length of ", repr(x), "is", len(x))
length_message('Fnord')
length_message([1, 2, 3])

  
__metaclass__ = type # 确定使用新式类
class Person:
    def setName(self, name):
        self.name = name 
    def getName(self):
        return self.name
    def greet(self):
        print("Hello, world! I'm %s." % self.name)
foo = Person()
bar = Person()
foo.setName('Luke Skywalker')
bar.setName('Anakin Skywalker')
foo.greet()
bar.greet()
print(foo.name)
bar.name = 'Yoda'
bar.greet()
  
  
class Class:
    def method(self):
        print('I have a self!')
def function():
        print("I don't ...")
instance = Class()
instance.method()
instance.method = function
instance.method()


class Bird:
    song = 'Squaawk!'
    def sing(self):
        print(self.song)
bird = Bird()
bird.sing()
birdsong = bird.sing
birdsong()


class Secretive:
    def __inaccesible(self):
        print("Bet you can't see me...")
    def accesible(self):
        print("The secret message is: ")
        self.__inaccesible()
s = Secretive()
#s.__inaccesible()
s.accesible() 
Secretive._Secretive__inaccessible
s._Secretive__inaccessible()


class MemberCounter:
    members = 0
    def init(self):
        MemberCounter.members += 1
m1 = MemberCounter()
m1.init()
#print(MemberCounter.members)
m2 = MemberCounter()
m2.init()
#print(MemberCounter.members)
print(m1.members)
print(m2.members)
m1.members = 'Two'
print(m1.members)
print(m2.members)


class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]
class SPAMFilter(Filter):   # SPAMFilter 是 Filter 的子类
    def init(self):     # 重写 Filter 超类中的 init 方法
        self.blocked = ['SPAM']
f = Filter()
f.init()
print(f.filter([1, 2, 3]))
s = SPAMFilter()
s.init()
#print(s.filter(['SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM']))
#print(issubclass(SPAMFilter, Filter))
#print(issubclass(Filter, SPAMFilter))
print(SPAMFilter.__bases__)
print(Filter.__bases__)
s = SPAMFilter()
print(isinstance(s, SPAMFilter))
print(isinstance(s, Filter))
print(isinstance(s, str))
print(s.__class__)


class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)
class Talker:
    def talk(self):
        print('Hi, my value is ', self.value)
class TalkingCalculator(Calculator, Talker):
    pass
tc = TalkingCalculator()
tc.calculate('1+2*3')
tc.talk()
print(hasattr(tc, 'talk'))
print(hasattr(tc, 'fnord'))
print(callable(getattr(tc, 'talk', None)))
print(callable(getattr(tc, 'fnord', None)))
setattr(tc, 'name', 'Mr. Gumby')
print(tc.name)


import exceptions
dir(exceptions)


while True:
    try:
        x = int(input('Enter the first number: '))
        y = int(input('Enter the second number: '))
        value = x/y
        print('x/y is ', value)
    except Exception as e:
        print('Invalid input: ', e)
        print('Please try again')
    else:
        break


class MuffledCalculator:
    muffled = False
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('Division by zero is illegal')
            else:
                raise
calculator = MuffledCalculator()
print(calculator.calc('10/2'))
#calculator.calc('10/0')     # No muffling
calculator.muffled = True
calculator.calc('10/0')


try:
    print('A simple task')
except:
    print('What? Something went wrong?')
else:
    print('Ah... It went as planned')


x = None
try:
    x = 1/0
finally:
    print('Cleaning up...')
    del x


try:
    1/0
except NameError:
    print("Unknown variable")
else:
    print("That went well!")
finally:
    print("Cleaning up.")


def faulty():
    raise Exception('Something is wrong')
def ignore_exception():
    faulty()
def handle_exception():
    try:
        faulty()
    except:
        print('Exception handled')
#ignore_exception()
handle_exception()


def describePerson(person):
    print('Description of', person['name'])
    print('Age:', person['age'])
#    if 'occupation' in person:
 #       print('Occupation:', person['occupation'])
    try:
        print('Occupation: ' + person['occupation'])
    except KeyError: pass


try:
    obj.write
except AttributeError:
    print('The object is not writeable')
else:
    print('The object is writeable')


class FooBar:
    def __init__(self, value=42):
        self.somevar = value
f = FooBar('This is a constructor argument')
print(f.somevar)


class A:
    def hello(self):
        print("Hello, I'm A.")
class B(A):
    def hello(self):
        print("Hello, I'm B.")
#a = A()
b = B()
#a.hello()
b.hello()


__metaclass__ = type # super 函数只在新式类中起作用
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaaah...')
            self.hungry = False
        else:
            print('No, thanks!')
#b = Bird()
#b.eat()
#b.eat()
class SongBird(Bird):
    def __init__(self):
       #Bird.__init__(self)
        super(SongBird, self).__init__()
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)
sb = SongBird()
sb.sing()
sb.eat()
sb.eat()


def checkIndex(key):
    if not isinstance(key, (int, int)): raise TypeError 
    if key<0: raise IndexError
class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        self.start = start      # 保存开始值
        self.step = step        # 保存步长值
        self.changed = {}       # 没有项背修改
    def __getitem__(self, key):
        checkIndex(key)
        try: return self.changed[key]   # 修改了吗？
        except KeyError:                # 否则。。。
            return self.start + key*self.step   # 计算值
    def __setitem__(self, key, value):
        checkIndex(key)
        self.changed[key] = value   # 保存更改后的值
s = ArithmeticSequence(1, 2)
print(s[4])
s[4] = 2
print(s[4])
print(s[-42])


class CounterList(list):
    def __init__(self, *args):
        super(CounterList, self).__init__(*args)
        self.counter = 0
    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)
cl = CounterList(range(10))
print(cl)
cl.reverse()
print(cl)
del cl[3:6]
print(cl)
print(cl.counter)       # counter 特性初始化为0，每次列表元素被访问时，它都会自增
print(cl[4] + cl[2])
print(cl.counter)

__metaclass__ = type  
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height
    size = property(getSize, setSize)
r = Rectangle()
r.width = 10
r.height = 5
print(r.size)
r.size = 150, 100
print(r.width)
  
  
__metaclass__ = type 
class MyClass:
    @staticmethod       # 使用 @ 操作符，在方法或函数的上方将装饰器（它能对任何可调用的对象进行包装，既能够用于方法也能用于函数）列出
    def smeth():
        print('This is a static method')
    #smeth = staticmethod(smeth)
    @classmethod 
    def cmeth(cls):
        print('This is a class method of ', cls)
    #cmeth = classmethod(cmeth)
MyClass.smeth()
MyClass.cmeth()


class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.height = value 
        else:
            self.__dict__[name] = value 
    def __getattr__(self, name):
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError


class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a, self.b = self.b, self.a+self.b
        return self.a
    def __iter__(self):
        return self
fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f)
        break

it = iter([1, 2, 3])
print(it.__next__())
print(it.__next__())


class TestIterator:
    value = 0
    def __next__(self):
        self.value += 1
        if self.value > 10: raise StopIteration
        return self.value
    def __iter__(self):
        return self
ti = TestIterator()
print(list(ti))


def flattern(nested):
    for sublist in nested:
        for element in sublist:
            yield element
nested = [[1, 2], [3, 4], [5]]
for num in flattern(nested):
    print(num)
print(list(flattern(nested)))


def flattern(nested):
    try:
        # 不要迭代类似字符串的对象：
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flattern(sublist):
                yield element 
    except TypeError:
        yield nested
print(list(flattern([[[1], 2], 3, 4, [5, [6, 7]], 8])))
print(list(flattern(['foo', ['bar', ['baz']]])))


def repeater(value):
    while True:
        new = (yield value)
        if new is not None: value = new
r = repeater(42)
print(r.__next__())
print(r.send("Hello, world!"))


def flattern(nested):
    result = []
    try:
        #不要迭代类似字符串的对象
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flattern(sublist):
                result.append(element)
    except TypeError:
        result.append(nested)
    return result


def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0, nextY-i):
            return True 
    return False
# def queens(num, state):
#     if len(state) == num-1:
#         for pos in range(num):
#             if not conflict(state, pos):
#                 yield pos
def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num-1:
                yield(pos, )
            else:
                for result in queens(num, state + (pos, )):
                    yield (pos, ) + result

# print(list(queens(3)))
# print(list(queens(4)))
# for solution in queens(8):
#     print(solution)
# print(len(list(queens(8))))
def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length-pos-1)
    for pos in solution:
        print(line(pos))
import random 
prettyprint(random.choice(list(queens(8))))

import sys 
sys.path.append('F:\workspace\hola world\src')
import hello2       # Windows>Preferences>PyDev>Editor>Code Analysis>imports
hello2.hello()


import hello2
hello2.hello()
hello2.test()
print(__name__)
print(hello2.__name__)


import sys, pprint
pprint.pprint(sys.path)     # pprint 能够提供更加智能的打印输出


import copy 
#print(dir(copy))    # dir 函数查看模块包含的内容，会将对象（以及模块的所有函数、类、变量等）的所有特性列出
print([n for n in dir(copy) if not n.startswith('_')])
print(copy.__all__)     # __all__ 包含一个列表，定义了模块的公有接口。
help(copy.copy)
print(copy.copy.__doc__)

print(range.__doc__)


print(copy.__file__)


# 反序打印命令行参数 reverseargs.py
import sys 
args = sys.argv[1:]
args.reverse()
print(' '.join(args))

import os 
#os.system(r'C:\"Program Files"\"Internet Explorer"\iexplore.exe')
os.startfile(r'C:\Program Files\Internet Explorer\iexplore.exe')


import webbrowser
webbrowser.open("http://www.python.org")


print(set(range(10)))
print(set([0, 1, 2, 3, 4, 5, 0, 1, 2, 3]))
print(set(['foe', 'fee', 'fie']))


a = set([1, 2, 3])
b = set([2, 3, 4])
print(a.union(b))
print(a | b)
c = a & b 
print(c.issubset(a))
print(c <= a)
print(c.issuperset(a)) 
print(c >= a)
print(a.intersection(b))
print(a & b)
print(a.difference(b))
print(a - b)
print(a.symmetric_difference(b))
print(a ^ b)
print(a.copy())
print(a.copy() is a)


from functools import reduce
mySets = []
for i in range(10):
    mySets.append(set(range(i, i+5)))
print(reduce(set.union, mySets))


a = set()
b = set()
#a.add(b)
print(a.add(frozenset(b)))


from heapq import *
from random import shuffle
# data = list(range(10))
# shuffle(data)
# heap = []
# for n in data:
#     heappush(heap, n)
# print(heap)
# heappush(heap, 0.5)
# print(heap)
# print(heappop(heap))
# print(heappop(heap))
# print(heappop(heap))
# print(heap)
heap = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2]
heapify(heap)
print(heap)
print(heapreplace(heap, 0.5))
print(heap)
print(heapreplace(heap, 10))
print(heap)


from collections import deque
q = deque(range(5))
q.append(5)
q.appendleft(6)
print(q)
print(q.pop())
print(q.popleft())
q.rotate(3)
print(q)
q.rotate(-1)
print(q)


import time
print(time.asctime())


from random import *
from time import *
date1 = (2008, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = mktime(date1)
date2 = (2009, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = mktime(date2)
random_time = uniform(time1, time2)
print(asctime(localtime(random_time)))


from random import randrange 
num = int(input('How many dice? '))
sides = int(input('How many sides per die? '))
sum = 0
for i in range(num): sum += randrange(sides) + 1
print('The result is ', sum)


values = list(range(1, 11)) + 'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['%s of %s' % (v, s) for v in values for s in suits]
from pprint import pprint 
pprint(deck[:12])
from random import shuffle
shuffle(deck)
pprint(deck[:12])


import shelve
s = shelve.open('test.dat')
s['x'] = ['a', 'b', 'c']
s['x'].append('d')
print(s['x'])
temp = s['x']
temp.append('d')
s['x'] = temp 
print(s['x'])


import re
# some_text = 'alpha. beta....gamma delta'
# print(re.split('[. ]+', some_text))
# print(re.split('o(o)', 'foobar'))
# print(re.split('[. ]+', some_text, maxsplit=2))
# print(re.split('[. ]+', some_text, maxsplit=1))
# pat = '[a-zA-Z]+'
# text = '"Hm... Err -- are you sure?" he said, sounding insecure.'
# print(re.findall(pat, text))
# pat = r'[.?\-",]+'
# print(re.findall(pat, text))
# pat = '{name}'
# text = 'Dear {name}...'
# print(re.sub(pat, 'Mr. Gumby', text))
# print(re.escape('www.python.org'))
# print(re.escape('But where is the ambiguity?'))
# m = re.match(r'www\.(.*)\..{3}', 'www.python.org')
# print(m.group(1))
# print(m.start(1))
# print(m.end(1))
# print(m.span(1))
#emphasis_pattern = r'\*([^\*]+)\*'
#emphasis_pattern = re.compile(r'''
#     \*    # Beginning emphasis tag    -- an asterisk
#     (    # Begin group for capturing phrase
#     [^\*]+    # Capture anythin except asterisks
#     )    # End group
#     \*    # Ending emphasis tag
#     ''', re.VERBOSE)        # VERBOSE 标识允许在模式中添加空白
from test.test_pdb import do_something
'''print(re.sub(emphasis_pattern, r'<em>\1<em>', 'Hello, *world*!'))
emphasis_pattern = r'\*(.+)\*'
print(re.sub(emphasis_pattern, r'<em>\1</em>', '*This* is *it*!'))  # <em>This* is *it</em>!
emphasis_pattern = r'\*\*(.+?)\*\*'
print(re.sub(emphasis_pattern, r'<em>\1</em>', '**This** is **it**!'))  # <em>This</em> is <em>it</em>!


f = open('somefile.txt', 'w')
f.write('Hello, ')
f.write('World!')
f.close()
f = open('somefile.txt', 'r')
print(f.read(4))
print(f.read())


f = open(r'somefile.txt', 'w')
f.write('01234567890123456789')
f.seek(5)
f.write('Hello, World!')
f.close
f = open(r'somefile.txt')
print(f.read())
f = open(r'somefile.txt')
print(f.read(3))
print(f.read(2))
print(f.tell())

with open("somefile.txt") as somefile:
    do_something(somefile)


f = open(r'somefile.txt')
print(f.read(7))
print(f.read(4))
f.close()
f = open(r'somefile.txt')
print(f.read())
f.close()
f = open(r'somefile.txt')
for i in range(3):
    print(str(i) + ': ' + f.readline())
f.close()
import pprint
pprint.pprint(open(r'somefile.txt').readlines())
f = open(r'somefile.txt', 'w')
f.write('this\nis no\nhaiku')
f.close
f = open(r'somefile.txt')
lines = f.readlines()
f.close()
lines[1] = "isn't a\n"
f = open(r'somefile.txt', 'w')
f.writelines(lines)
f.close()


def process(string):
    print('Processing: ', string)
#f = open(r'somefile.txt')

# while True:
#     char = f.read(1)
#     if not char: break
#     process(char)
# f.close()

# while True:
#     line = f.readline()
#     if not line: break
#     process(line)
# f.close()

# for char in f.read():
#     process(char)
# f.close

# for line in f.readlines():
#     process(line)
# f.close()

# import fileinput
# for line in fileinput.input(r'somefile.txt'):
#     process(line)

# for line in f:
#     process(line)
# f.close()

# for line in open(r'somefile.txt'):
#     process(line)

# import sys 
# for line in sys.stdin:
#     process(line)

# f = open('somefile.txt', 'w')
# f.write('First line\n')
# f.write('Second line\n')
# f.write('Third line\n')
#f.close()
lines = list(open('somefile.txt'))
print(lines)
first, second, third = open('somefile.txt')
print(first,)
print(second,)
print(third,)


import sqlite3
conn = sqlite3.connect('somedatabase.db')
curs = conn.cursor()
conn.commit()
conn.close()


from urllib.request import urlopen, urlretrieve
webpage = urlopen('http://www.python.org')
#print(webpage)
import re 
text = webpage.read()
m = re.search('<a href="([^"]+)" .*?>about</a>', text, re.IGNORECASE)
m.group(1)
urlretrieve('http://python.org', 'C:\\python_webpage.html')


from urllib.request import urlopen
import re
p = re.compile('<h3><a .*?><a .*? href="(.*?)">(.*?)</a>')
text = urlopen('http://www.python.org/community/jobs').read()
for url, name in p.findall(text):
    print('%s (%s)' % (name, url))


from subprocess import Popen, PIPE
text = open('messy.html').read()
tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE)
tidy.stdin.write(text)
tidy.stdin.close()
print(tidy.stdout.read())


import cgitb; cgitb.enable()
print('Content-type: text/html')
print()
print(1/0)
print('Hello, world!')


# import cgi
# form = cgi.FieldStorage()
# name = form.getvalue('name', 'world')
# 
# print("""Content-type: text/html
# <html>
#     <head>
#         <title>Greeting Page</title>
#     </head>
#     <body>
#         <h1>Hello, %s!</h1>
#         <form action='simple3.cgi'>
#         Change name <input type='text' name='name'/>
#         <input type='submit'/>
#         </form>
#     </body>
# </html>
# """ % name) 


# 带有少量随机数据的 PSP 例子
<%
from random import choice
adjectives = ['beautiful','cruel']
%>
<html>
    <head>
        <title>Hello</title>
    </head>
    <body>
    <p>Hello, <%=choice(adjectives)%>world. My name is Mr. Gumby.</p>
    </body>
</html>


from area import rect_area
height = 3
width = 4
correct_answer = 12
answer = rect_area(height, width)
if answer == correct_answer:
    print('Test passed')
else:
    print('Test failed')


from distutils.core import setup
setup(name='Hello',
      version='1.0',
      description='A simple example',
      author='LIU',
      py_modules=['hello'])


from distutils.core import setup
import py2exe
setup(console=['hello.py'])


from configparser import ConfigParser


import logging
logging.basicConfig(level=logging.INFO, filename='mylog.log')
logging.info('Starting program')
logging.info('Trying to divide 1 by 0')
print(1 / 0)
logging.info('The division succeeded')
logging.info('Ending program')
'''

import reportlab









