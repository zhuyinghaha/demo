#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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


