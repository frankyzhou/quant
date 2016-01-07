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
type(a)

# 通过函数"reshape"，我们可以重新构造一下这个数组，例如，我们可以构造一个4*5的二维数组，
# 其中"reshape"的参数表示各维度的大小，且按各维顺序排列（两维时就是按行排列，这和R中按列是不同的）：
a = a.reshape(4, 5)#二维
print a
a = a.reshape(2, 2, 5)#更高维度（三维）
print a

# 既然a是array，我们还可以调用array的函数进一步查看a的相关属性："ndim"查看维度；"shape"查看各维度的大小；
# "size"查看全部的元素个数，等于各维度大小的乘积；"dtype"可查看元素类型；"dsize"查看元素占位（bytes）大小。
print a.ndim