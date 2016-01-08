# coding=utf-8
# 一，SciPy概述
# SciPy基于NumPy提供了更为丰富和高级的功能扩展，在统计、优化、插值、
# 数值积分、时频转换等方面提供了大量的可用函数，基本覆盖了基础科学计算相关的问题。
# 在量化分析中，运用最广泛的是统计和优化的相关技术，本篇重点介绍SciPy中的统计和优化模块，其他模块在
# 随后系列文章中用到时再做详述。

import numpy as np
import scipy.stats as stats
import scipy.optimize as opt

# 二，统计部分
# 2.1 生成随机数
# 我们从生成随机数开始，这样方便后面的介绍。生成n个随机数可用rv_continuous.rvs(size=n)或rv_discrete.rvs(size=n)，
# 其中rv_continuous表示连续型的随机分布，如均匀分布（uniform）、正态分布（norm）、贝塔分布（beta）等；
# rv_discrete表示离散型的随机分布，如伯努利分布（bernoulli）、几何分布（geom）、泊松分布（poisson）等。
# rvs是特定分布的随机变量组

# 均匀分布是介于loc,与loc+scale之间的均匀分布
rv_unif = stats.uniform.rvs(size=10, loc=3, scale=2)
unif = stats.uniform(3,2)
print "均匀分布:"
print rv_unif
print unif.rvs(10)

# 贝塔分布
rv_beta = stats.beta.rvs(size=10, a=4, b=2)
print "贝塔分布："
print rv_beta

# 正态分布:loc是均值，scale是方差
rv_norm = stats.norm.rvs(size=10, loc=1, scale=1)
print "正态分布："
print rv_norm

# 伯努利分布
rv_bern = stats.bernoulli.rvs(size=10, p=0.5)
print "伯努利分布:"
print rv_bern

# 二项式分布
rv_binom = stats.binom.rvs(size=20, n=20, p=0.5)
print "二项式分布:"
print rv_binom
