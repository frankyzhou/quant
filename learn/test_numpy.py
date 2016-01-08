# coding=utf-8

# 一、NumPy是什么？
# 量化分析的工作涉及到大量的数值运算，一个高效方便的科学计算工具是必不可少的
# 。Python语言一开始并不是设计为科学计算使用的语言，随着越来越多的人发现Python的易用性，
# 逐渐出现了关于Python的大量外部扩展，NumPy (Numeric Python)就是其中之一。NumPy提供了
# 大量的数值编程工具，可以方便地处理向量、矩阵等运算，极大地便利了人们在科学计算方面的工作。
# 另一方面，Python是免费，相比于花费高额的费用使用Matlab，NumPy的出现使Python得到了更多人的青睐。

import numpy as np

# 二、初窥NumPy对象：数组
# NumPy中的基本对象是同类型的多维数组（homogeneous multidimensional array），
# 这和C++中的数组是一致的，例如字符型和数值型就不可共存于同一个数组中。先上例子：
# 这里我们生成了一个一维数组a，从0开始，步长为1，长度为20。Python中的计数是从0开始的，
# R和Matlab的使用者需要小心。可以使用print查看：
a = np.arange(20)
print a
print type(a)

# 通过函数"reshape"，我们可以重新构造一下这个数组，例如，我们可以构造一个4*5的二维数组，
# 其中"reshape"的参数表示各维度的大小，且按各维顺序排列（两维时就是按行排列，这和R中按列是不同的）：
a = a.reshape(4, 5)#二维
print a
a = a.reshape(2, 2, 5)#更高维度（三维）
print a

# 既然a是array，我们还可以调用array的函数进一步查看a的相关属性："ndim"查看维度；"shape"查看各维度的大小；
# "size"查看全部的元素个数，等于各维度大小的乘积；"dtype"可查看元素类型；"dsize"查看元素占位（bytes）大小。
print a.ndim, a.shape, a.size, a.dtype

# 三、创建数组
# 数组的创建可通过转换列表实现，高维数组可通过转换嵌套列表实现：
raw = [0,1,2,3,4]#列表
print type(raw)
a = np.array(raw)
print type(a)
raw = [[0,1,2,3,4], [5,6,7,8,9]]
b = np.array(raw)
print b
print type(b)

# 一些特殊的数组有特别定制的命令生成，如4*5的全零矩阵：
d = (4, 5)#元祖
print type(d)
np.zeros(d)
np.ones(d, dtype=int)#默认生成的类型是浮点型，可以通过指定类型改为整型：
np.random.rand(5)#[0, 1)区间的随机数数组

# 四、数组操作
# 简单的四则运算已经重载过了，全部的'+'，'-'，'*'，'/'运算都是基于全部的数组元素的，以加法为例：
a = np.array([[1.0, 2], [2, 4]])
print "a:"
print a
b = np.array([[3.2, 1.5], [2.5, 4]])
print "b:"
print b
print "a+b:"
print a+b
print "3 * a:"
print 3 * a
print "b + 1.8:"
print b + 1.8
a /= 2#类似C++，'+='、'-='、'*='、'/='操作符在NumPy中同样支持
print a
# 开根号求指数也很容易
print "a:"
print a
print "np.exp(a):"
print np.exp(a)
print "np.sqrt(a):"
print np.sqrt(a)
print "np.square(a):"
print np.square(a)
print "np.power(a, 3):"
print np.power(a, 3)
# 二维数组的最大最小值,计算全部元素的和、按行求和
a = np.arange(20).reshape(4,5)
print "a:"
print a
print "sum of all elements in a: " + str(a.sum())
print "maximum element in a: " + str(a.max())
print "minimum element in a: " + str(a.min())
print "maximum element in each row of a: " + str(a.max(axis=1))
print "minimum element in each column of a: " + str(a.min(axis=0))

# 科学计算中大量使用到矩阵运算，除了数组，NumPy同时提供了矩阵对象（matrix）。
# 矩阵对象和数组的主要有两点差别：一是矩阵是二维的，而数组的可以是任意正整数维；
# 二是矩阵的'*'操作符进行的是矩阵乘法，乘号左侧的矩阵列和乘号右侧的矩阵行要相等，
# 而在数组中'*'操作符进行的是每一元素的对应相乘，乘号两侧的数组每一维大小需要一致。
# 数组可以通过asmatrix或者mat转换为矩阵，或者直接生成也可以：
a = np.arange(20).reshape(4, 5)
a = np.asmatrix(a)
print type(a)

b = np.matrix('1.0 2.0; 3.0 4.0')
print type(b)