#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码


# print(1+2+3);

# name = input();
# print('hello,',name);

# str = 'I\'m "OK"!';
# print(str);

# print(r'''line1
# line2
# line3''')

# print(r'''hello,\n
# world''')

# age = 19
# if age >= 18:
#     print(1111)
# else:
#     print(2222)
# a = 'ABC'
# b = a
# a = 'XYZ'
# print(b)

# print('你好么')

# print('%2d-%02d' % (3, 1))
# print('%.2f' % 3.1415926)

# str = 1 + \
# 2+\
# 3
# print(str)



############################   有序列表 list和tuple ##################################
# classmates = ['Michael', 'Bob', 'Tracy']
# classmates.append('amber');#插入末尾
# classmates.insert(1,'two');
# classmates.pop(0);#没有index删除末尾，有index就是对应位置
# print(classmates);
# print(len(classmates));

# L = ['Apple', 123, True]
# print(L)

# p = ['asp', 'php']
# s = ['python', 'java', p, 'scheme']
# print(s)
# print(s[2][1])

#L = []
# print(len(L))


######## tuple
######## 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
# 没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，
# 你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素
# classmates = ('Michael', 'Bob', 'Tracy')
# t = (1,)  # t = (1)表示数学上面小括号，结果表示 1
# print(t)

############################ 条件判断 ##################################
# 注意:
# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:

# age = 20
# if age > 20:
#     print('age111')
# elif age>18:
#     print('age18-20')
# else:
#     print('age000')

# birth = int(input('please input birth:'))
# if birth < 2000:
#     print('<2000')

############################ 循环 ##################################
###### for循环
# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#     print(name)
# range(5)生成的序列是从0开始小于5的整数
# list = list(range(101))
# # print(list)
# sum = 0
# for x in list:
#     sum = sum + x
# print(sum)

##### while循环
# sum = 0
# n = 9
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)

##### break 可以提前退出循环
##### 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环
#循环是让计算机做重复任务的有效的方法。
#break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。
#要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。
#大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。
#有些时候，如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。这时可以用Ctrl+C退出程序，或者强制结束Python进程。


############################ dict和set ##################################

# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
# 如果key不存在，dict就会报错
# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value

#请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的

# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# d['Adam'] = 67
# print(d)
# print('Thomas' in d) # False
# print(d.get('Thomas')) # None 返回None的时候Python的交互环境不显示结果
# print(d.get('Thomas', -1)) # -1
# d.pop('Bob')
# print(d)

### set  也是一组key的集合，但不存储value.   由于key不能重复，所以，在set中，没有重复的key
# set可以看成数学意义上的无序和无重复元素的集合
# 因此，两个set可以做数学意义上的交集、并集等操作
# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，
# 因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。
# s = set([1, 2, 2, 3, 3])
# s.add(4)
# s.remove(1)
# print(s)

# 再议不可变对象
# 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。
# 相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
# d = {}
# key = (1, 2, 3) # tuple
# d[key] = 23
# print(d) #{(1, 2, 3): 23}
# key = (1, [2, 3])
# d[key] = 25
# print(d) #报错 

# s = set((1,2,3))
# print(s) #{1, 2, 3} 元素中没有list的tuple和list一样，可以作为set输入集合
# s = set(1,[2,3])
# print(s) # wrong 结论：元素中有list的tuple不可作为set的输入集合。因为，set是将list或者tuple里每一个不重复的元素作为一个key（
#          # 这里只是将list当前的元素输入到key上，指定key后，原来的list怎么变都行）如果tuple元素有list，那么[2,3]这个list就成为了一个key。
#          # 而[2,3]只是在tuple的指向不变。而key必须是不可变对象，所以报错。


###############################  函数   #####################
# str = 111
# print(hex(str))
# x = abs(100)
# y = abs(-20)
# print(x, y)
# print('max(1, 2, 3) =', max(1, 2, 3))
# print('min(1, 2, 3) =', min(1, 2, 3))
# print('sum([1, 2, 3]) =', sum([1, 2, 3]))
# print('sum((1, 2, 3)) =', sum((1, 2, 3)))

# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x

# 引入函数
# from abstest import my_abs
# print(my_abs(-1))

# 在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标
# import math
# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny

# r = move(100, 100, 60, math.pi / 6)
# print(r)

# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0 的两个解。

# import math
# def quadratic(a, b, c):
#     for i in a,b,c:
#         if not isinstance(i,(int ,float)):
#             raise TypeError('bad operate type')
#     if a == 0:
#         raise TypeError('a不能为0')
#     d = math.pow(b, 2) - 4 * a * c

#     if d < 0:
#         print("无实数根")
#     elif d == 0:
#         x = -b/(2 * a)
#         print('root=%s' % str(x))
#         return root
#     else:
#         root1 = (-b + math.sqrt(d)) / (2 * a)
#         root2 = (-b - math.sqrt(d)) / (2 * a)
#         print("root1=", root1)
#         print("root2=", root2)
#         return root1,root2

# #quadratic(a, b, c)


# # 测试:
# print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

# if quadratic(2, 3, 1) != (-0.5, -1.0):
#     print('测试失败')
# elif quadratic(1, 3, -4) != (1.0, -4.0):
#     print('测试失败')
# else:
#     print('测试成功')


#以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积
# def product(x, *ys):
#     #print(ys)
#     sum = x
#     for y in ys:
#         #print(y)
#         sum = sum * y
#     return sum  

# # 测试
# print('product(5) =', product(5))
# print('product(5, 6) =', product(5, 6))
# print('product(5, 6, 7) =', product(5, 6, 7))
# print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
#     print('测试失败!')
# elif product(5, 6) != 30:
#     print('测试失败!')
# elif product(5, 6, 7) != 210:
#     print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         product()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')


#########  递归函数  #########
#汉诺塔移动
#我一开始很难理解move里面4个参数的意思和相互之间的关系
#后来发现move(n,a,b,c)可以翻译成：
#把n个盘子，借助b(第3个参数)，从a(第2个参数)移到c(第4个参数)
# def move(n, a, b, c): 
#     if n == 1:   # 如果a只有1盘子
#         print(a, '-->', c);   # 直接把盘子从a移到c
#     else:   # 如果a有n个盘子(n > 1)，那么分三步
#         move(n-1, a, c, b)   # 先把上面n-1个盘子，借助c，从a移到b
#         move(1, a, b, c)   # 再把最下面的1个盘子，借助b，从a移到c
#         move(n-1, b, a, c)   # 最后把n-1个盘子，借助a，从b移到c
# move(3,'A','B','C')  # 测试


#######################   高级特性    ###################
# 切片
# 取list前三个
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# r = []
# n = 3
# for i in range(n):
#     r.append(L[i])
# print(list(range(n))) #0-n的队列
# print(r)

# print(L[0:3]) #L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素
# print(L[:3])  #如果第一个索引是0，还可以省略
# #既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
# #记住倒数第一个元素的索引是-1
# print(L[-2:])
# print(L[-2:-1])

# L = list(range(10))
# print(L) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(L[:10:2]) #前10个数，每两个取一个
# print(L[::5]) #所有数，每5个取一个
# print(L[:]) #甚至什么都不写，只写[:]就可以原样复制一个list

# t = (0, 1, 2, 3, 4, 5)
# print(t[:2])

# print('ABCDEFG'[:3])

##### 小试牛刀
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
# def trim(s):
#     if s[:1] == ' ':
#         return trim(s[1:])
#     elif s[-1:] == ' ':
#         return trim(s[:-1])
#     else:
#         return s
# 测试:  用到了递归
# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')


# 迭代
# d = {'a': 1, 'b': 2, 'c': 3} 
# for key in d:  #迭代的是key
#     print(key)
# for value in d.values():  #迭代的是value
#     print(value)
# 同时迭代key和value，可以用for k, v in d.items()
# for k, v in d.items():
#     print(k,v)

# 字符串 迭代
# for ch in 'ABC':
#     print(ch)

# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)

# for x, y in [(1, 1), (2, 4), (3, 9)]:
#     print(x, y)

### 练习
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple
# def findMinAndMax(L):
#     if len(L) > 0:
#         max = L[0]
#         min = L[0]
#         for i, value in enumerate(L):
#             if max < value:
#                 max = value
#             elif min > value:
#                 min = value
#         return (min, max)
#     return (None, None)

# # 测试
# if findMinAndMax([]) != (None, None):
#     print('测试失败1!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败2!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败3!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败4!')
# else:
#     print('测试成功!')


## 列表生成式
# print([x * x for x in range(1,11)])
# print([m + n for m in 'ABC' for n in 'XY'])

# import os # 导入os模块，模块的概念后面讲到
# print([d for d in os.listdir('.')]) # os.listdir可以列出文件和目录


###  练习
#如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错

#请修改列表生成式，通过添加if语句保证列表生成式能正确地执行
# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [i.lower() for i in L1 if isinstance (i,str)]
# # 测试:
# print(L2)
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')


## 生成器
# g = (x * x for x in range(10))
# # print(g)
# # print(next(g))
# for i in g:
#     print(i)

#比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
#1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# fib(6)

# 仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
# 也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# f = fib(6)
# print(f)

# 举个简单的例子，定义一个generator，依次返回数字1，3，5：
# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield(3)
#     print('step 3')
#     yield(5)

# o = odd()
# print(next(o))
# print(next(o))
# print(next(o))
# print(next(o))


# g = fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break


### 练习
# 杨辉三角定义如下：
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list：

# def triangles():
#     L = [1]
#     while True:
        # yield L
        # #不能用append的原因是用append,地址没有变，在results.append(t)后，再执行L.append(0)，results内的t也会变
        # #L.append(0)
        # L = L + [0]
        # L = [(L[i-1]+L[i]) for i in range(len(L))]

# def triangles():
#     cur = [1]
#     n = 0
#     while True:
#         yield cur
#         temp = [1]
#         for i in range(n):
#             x = cur[i] + cur[i + 1]
#             temp.append(x)
#         temp.append(1)
#         cur = temp
#         n = n + 1
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# n = 0
# results = []
# for t in triangles():
#     print(t)
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')




###  iterable  迭代器
# from collections import Iterable
# print(isinstance([],Iterable))


#函数式编程
# def add(x, y, f):
#     return f(x) + f(y)

# print(add(-5, 6, abs))


# print(sum([1,2,3,4,5]))

# from functools import reduce
# def fn(x, y):
#     return x * 10 + y

# print(reduce(fn, [1, 3, 5, 7, 9]))


#考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数
# from functools import reduce
# def fn(x, y):
#     return x * 10 + y

# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]

# # print(list(map(char2num, '13579')))    ##[1, 3, 5, 7, 9]
# print(reduce(fn, map(char2num, '13579')))

# #整理成一个str2int的函数
# from functools import reduce

# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(fn, map(char2num, s))

# #还可以用lambda函数进一步简化成
# from functools import reduce

# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

# def char2num(s):
#     return DIGITS[s]

# def str2int(s):
#     return reduce(lambda x, y: x * 10 + y, map(char2num, s))



#练习
#1. 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# def normalize(name):
#     q = name[0].upper()
#     w = name[1:].lower()
#     return q + w
   
# # 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)


#2. Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
# from functools import reduce

# def prod(L):
#     def fn(x, y):
#         return x * y
#     return reduce(fn, L)

    
# # 测试：
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')


#3. 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# from functools import reduce
# def str2float(s):
#     def fn(x,y):
#         return x * 10 + y
#     def char2num(s):
#         DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#         return DIGITS[s]
#     temp = s.split('.')    
#     sleft = temp[0]
#     sright = temp[1]
#     return reduce(fn,map(char2num,sleft)) + reduce(fn,map(char2num,sright)) / (10**s.index('.'))

# #练习：
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')



###  filter()
# def is_odd(n):
#     return n % 2 == 1

# print(list(filter(is_odd, [1, 2, 3, 4, 5, 6])))

# def not_empty(s):
#     return s and s.strip()
# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


# 用filter求素数
# 计算素数的一个方法是埃氏筛法
# 用Python来实现这个算法，可以先构造一个从3开始的奇数序列：

# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
# # 注意这是一个生成器，并且是一个无限序列。

# # 然后定义一个筛选函数：
# def _not_divisible(n):
#     return lambda x: x % n > 0

# # 最后，定义一个生成器，不断返回下一个素数：
# def primes():
#     yield 2
#     it = _odd_iter() # 初始序列
#     while True:
#         n = next(it) # 返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n), it) # 构造新序列

# # 打印1000以内的素数:
# for n in primes():
#     if n < 20:
#         print(n)
#     else:
#         break

#练习
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
# def is_palindrome(n):
#     sn = str(n)
#     lens = len(sn)
#     for i,value in sn:
#         if sn[i] != sn[lens-1]:
#             return false
#             break
#     return true

# def is_palindrome(n):
#     s=str(n)
#     return s==s[::-1]



# # 测试:
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')


#练习
#假设我们用一组tuple表示学生名字和成绩：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# #请用sorted()对上述列表分别按名字排序：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# def by_name(t):
#     return t[0].lower()

# def by_score(s):
#     return s[-1]

# L2 = sorted(L, key=by_name)
# print(L2)
# L3 = sorted(L, key=by_score)
# print(L3) 



## 闭包
#练习
#利用闭包返回一个计数器函数，每次调用它返回递增整数：
# def createCounter():
#     count = 0
#     def counter():
#         nonlocal count
#         count = count + 1
#         return count
#     return counter

# # 测试:
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')


#匿名函数
#练习
#请用匿名函数改造下面的代码：
# def is_odd(n):
#     return n % 2 == 1

# L = list(filter(lambda x: x % 2 , range(1, 20)))
# print(L)

#装饰器
#练习
#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
# import time, functools
# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args, **kw):
#         start = time.time()
#         stop = time.time()-start
#         print('%s executed in %s ms' % (fn.__name__, stop))
#         return fn(*args, **kw)
#     return wrapper
   

# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;

# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;

# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')


###########  模块   
#我们以内建的sys模块为例，编写一个hello的模块
# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-     #第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码

# ' a test module '    #是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

# __author__ = 'Michael Liao'  #使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名

# #以上就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错

# import sys

# def test():
#     args = sys.argv
#     if len(args)==1:
#         print('Hello, world!')
#     elif len(args)==2:
#         print('Hello, %s!' % args[1])
#     else:
#         print('Too many arguments!')

# if __name__=='__main__':
#     test()



######  面向对象
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'

# lisa = Student('Lisa', 99)
# bart = Student('Bart', 59)
# print(lisa.name, lisa.get_grade())
# print(bart.name, bart.get_grade())



#练习
# #请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender

#     def get_gender(self):
#         return self.__gender

#     def set_gender(self, gender):
#         self.__gender = gender


# # 测试:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')



### 实例属性和类属性
#练习
#为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
# class Student(object):
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         Student.count += 1

# # 测试:
# if Student.count != 0:
#     print('测试失败11!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')


#面向对象高级编程
# class Student(object):
#     pass


#尝试给实例绑定一个属性
#方法1
# s = Student()
# #s.name = 'xiaoying'
# #print(s.name)
# #方法2
# def set_age(self, age): # 定义一个函数作为实例方法
#         self.age = age

# from types import MethodType
# s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
# s.set_age(25) # 调用实例方法
# print(s.age) # 测试结果



###  __slots__ 
# class Student(object):
#     __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

# s = Student() # 创建新的实例
# s.name = 'Michael' # 绑定属性'name'
# s.age = 25 # 绑定属性'age'
# #s.score = 99 # 绑定属性'score'

# class GraduatesStudent(Student):
#         pass
# g = GraduatesStudent()
# g.name = '111'
# g.score = 20
# print(g.score)


### 练习
# class Student(object):
#     pass

# def set_age(self, age):
#     self.age = age

# from types import MethodType
# #给实例增加属性
# s1 = Student()
# s1.set_age = MethodType(set_age, s1)
# s1.set_age(11)
# print(s1.age) #11

# #给类增加属性一
# Student.set_age = MethodType(set_age, Student)
# Student.set_age(22)
# print(Student.age) #22
# s2 = Student()
# s3 = Student()
# s2.set_age(33)
# s3.set_age(44)
# print(s2.age, s3.age) #44 #44 s3覆盖s2

# #给类增加属性二
# Student.set_age = set_age
# Student.set_age(Student, 55)
# print(Student.age) #55
# s4 = Student()
# s5 = Student()
# s4.set_age(66)
# s5.set_age(77)
# print(s4.age, s5.age) #66 #77 互不干扰


### 使用@property
# class Student(object):
#     def get_score(self):
#          return self._score

#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value

# s = Student()
# s.set_score(60) # ok!
# s.get_score()
# print(s.get_score())
# #s.set_score(9999)

###  改编上面的方法 使用decorator装饰器
# class Student(object):

#     @property
#     def score(self):
#         return self._score

#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value

# s = Student()
# s.score = 60 # OK，实际转化为s.set_score(60)
# print(s.score) # OK，实际转化为s.get_score()

## 设置只读属性
# class Student(object):

#     @property
#     def birth(self):
#         return self._birth

#     @birth.setter
#     def birth(self, value):
#         self._birth = value

#     @property
#     def age(self):
#         return 2015 - self._birth


#练习
#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
# class Screen(object):
#     @property
#     def width(self):
#         return self._width

#     @width.setter
#     def width(self, value):
#         self._width = value

#     @property
#     def height(self):
#         return self._height

#     @height.setter
#     def height(self, value):
#         self._height = value
    
#     @property
#     def resolution(self):
#         self._resolution = self._width * self._height
#         return self._resolution

# # 测试:
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')


### 多重继承

# 关于多重继承,其实,只要了解拓扑排序,就能很清楚的指导多重继承的查询顺序了,从入度为0的位置起,剪掉入度为0相关边,
# 然后接着找下一个入度为0的位置,如此往复到最后,遇到有多个入度为0的时候,按最左原则取就行了,大体上就是这样了

# mro,解析方法调用的顺序

# class A(object):
#     def foo(self):
#         print('A foo')
#     def bar(self):
#         print('A bar')

# class B(object):
#     def foo(self):
#         print('B foo')
#     def bar(self):
#         print('B bar')

# class C1(A,B):
#     pass

# class C2(A,B):
#     def bar(self):
#         print('C2-bar')

# class D(C1,C2):
#     pass

# if __name__ == '__main__':
#     print(D.__mro__)
#     d=D()
#     d.foo()
#     d.bar()


### 定制类
# __iter__   用于类循环

# 以 斐波那契数列 为例
# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1 # 初始化两个计数器a，b

#     def __iter__(self):
#         return self # 实例本身就是迭代对象，故返回自己

#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b # 计算下一个值
#         if self.a > 100000: # 退出循环的条件
#             raise StopIteration()
#         return self.a # 返回下一个值

# # 循环斐波那契数列
# for i in Fib():
#         print(i)


# __getitem__  
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法： 
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
#现在，就可以按下标访问数列的任意一项了
f = Fib()
print(f[0])



###  list 切片









