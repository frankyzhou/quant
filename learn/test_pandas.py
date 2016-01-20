# coding=utf-8
# 一、Pandas介绍
# 在处理实际的金融数据时，一个条数据通常包含了多种类型的数据，例如，股票的代码是字符串，
# 收盘价是浮点型，而成交量是整型等。在C++中可以实现为一个给定结构体作为单元的容器，
# 如向量（vector，C++中的特定数据结构）。在Python中，pandas包含了高级的数据结构
# Series和DataFrame，使得在Python中处理数据变得非常方便、快速和简单。
import pandas as pd

# pandas主要的两个数据结构是Series和DataFrame，随后两节将介绍如何由其他类型的
# 数据结构得到这两种数据结构，或者自行创建这两种数据结构，我们先导入它们以及相关模块：
import numpy as np
from pandas import Series, DataFrame

# 二、Pandas数据结构：Series
# 从一般意义上来讲，Series可以简单地被认为是一维的数组。Series和一维数组最主要的区别在于
# Series类型具有索引（index），可以和另一个编程中常见的数据结构哈希（Hash）联系起来。

# 2.1 创建Series
# 创建一个Series的基本格式是s = Series(data, index=index, name=name)
a = np.random.randn(5)
print "a is an array:"
print a
s = Series(a)
print "s is a Series:"
print s
# 可以在创建Series时添加index，并可使用Series.index查看具体的index。需要注意的一点是，
# 当从数组创建Series时，若指定index，那么index长度要和data的长度一致：
s = Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print s
print s.index
# Series还可以从字典（dict）创建：
d = {'a': 0., 'b': 1, 'c': 2}
print "d is a dict:"
print d
s = Series(d)
print "s is a Series:"
print s

# 2.2 Series数据的访问
# 访问Series数据可以和数组一样使用下标，也可以像字典一样使用索引，
# 还可以使用一些条件过滤：
s = Series(np.random.randn(10),index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
s[0]
s[:2]
s[[2,1,4]]
s[['e','i']]
s[s>0.5]
'e' in s

# 三、Pandas数据结构：DataFrame
# 在使用DataFrame之前，我们说明一下DataFrame的特性。DataFrame是将数个Series按列合并而成的二维数据结构，
# 每一列单独取出来是一个Series，这和SQL数据库中取出的数据是很类似的。所以，按列对一个DataFrame进行处理更为方便，
# 用户在编程时注意培养按列构建数据的思维。DataFrame的优势在于可以方便地处理不同类型的列，因此，就不要考虑如何对
# 一个全是浮点数的DataFrame求逆之类的问题了，处理这种问题还是把数据存成NumPy的matrix类型比较便利一些。
# 3.1 创建DataFrame
# 首先来看如何从字典创建DataFrame。DataFrame是一个二维的数据结构，是多个Series的集合体。我们先创建一个值是Series的字典，
# 并转换为DataFrame：
d = {'one': Series([1., 2., 3.], index=['a', 'b', 'c']), 'two': Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = DataFrame(d)
print df
# 可以指定所需的行和列，若字典中不含有对应的元素，则置为NaN：
df = DataFrame(d, index=['r', 'd', 'a'], columns=['two', 'three'])
print df
print "DataFrame index:"
print df.index
print "DataFrame columns:"
print "DataFrame columns:"
print df.columns
print "DataFrame values:"
print df.values

# 3.2 DataFrame数据的访问
# 首先，再次强调一下DataFrame是以列作为操作的基础的，全部操作都想象成先从DataFrame里取一列，再从这个Series取元素即可。
# 可以用datafrae.column_name选取列，也可以使用dataframe[]操作选取列，我们可以马上发现前一种方法只能选取一列，而后一种方法可以选择多列。
# 若DataFrame没有列名，[]可以使用非负整数，也就是“下标”选取列；若有列名，则必须使用列名选取，另外datafrae.column_name在没有列名的时候是无效的：
print df["two"]
print type(df['two'])
print df.two

# 设置输出宽度
pd.set_option('display.width', 200)

# 创建一个以日期为元素的Series：
dates = pd.date_range('20141230', periods=5)
print dates

# 只要是能转换成Series的对象，都可以用于创建DataFrame：
df = pd.DataFrame(np.random.randn(5, 4),index=dates,columns=list('ABCD'))
print df
df = pd.DataFrame(np.random.randn(4, 5),index=list('ABCD'),columns=dates)
print df

print df.describe()