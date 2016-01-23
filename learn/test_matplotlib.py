# coding=utf-8

# matplotlib大概是被使用最多的二维绘图Python包。
# 它不仅提供一个非常快捷的用python可视化数据的方法，而且提供了出版质量的多种格式图像。

# pylab
# pylab提供了一个针对matplotlib面向对象绘图库的程序界面。
# 它模仿Matlab(TM)开发。因此，pylab大部分的绘图命令和参数和Matlab(TM)相似。重要的命令被交互示例解释。

# matplotlib有一套允许定制各种属性的默认设置。
# 你可以几乎控制matplotlib中的每一个默认属性：图像大小，每英寸点数，
# 线宽，色彩和样式，子图(axes)，坐标轴和网格属性，文字和字体属性，等等。
# 虽然matplotlib的默认设置在大多数情况下相当好，你却可能想要在一些特别的情形下更改一些属性。

# import numpy as np
from pylab import *

# 正炫，余弦曲线
# Create a new figure of size 8x6 points, using 80 dots per inch
figure(figsize=(10,6), dpi=80)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

# Create a new subplot from a grid of 2x2
# 第一个数字是行号，第二个数字是列号，第三个是序号。
# 写成（221）和（2，2,1）皆可
subplot(331)
title('1')
# Plot cosine using blue color with a continuous line of width 1 (pixels)
plot(X, C, color="blue",  linestyle="--")

# Plot sine using green color with a continuous line of width 1 (pixels)
plot(X, S, color="green", linewidth=1.0, linestyle="-")

# Set x limits
# xlim(-4.0,4.0)

# Set x ticks：刻度
xticks(np.linspace(-4,4,3,endpoint=True))

# Set y limits
# ylim(-1.0,1.0)

# Set y ticks
yticks(np.linspace(-1,1,5,endpoint=True))

# Save figure using 72 dots per inch
# savefig("exercice_2.png",dpi=72)

# 当前的图像边界有点太紧了一点，而且我们想要预留一点空间使数据点更清晰
# xlim(X.min()*1.5, X.max()*1.5)
# ylim(C.min()*1.1, C.max()*1.1)

# 当前刻度并不理想，因为它们不显示正余弦中我们感兴趣的值(+/-π,+/-π/2)。我们将更改它们让它们只显式这些值。
# xticks( [-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
# yticks([-1, 0, +1])

subplot(332)
# 刻度已经放置合适但是他们的标签并不很清楚，我们可以猜出3.142是π但是最好让它更直接。当我们设置刻度值时，
# 我们也可以在第二个参数列表中提供相应的标签。注意，我们用latex获得更好渲染的标签。
xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2+\pi$'])
yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])

plot(X, C, color="blue",  linestyle="--")
plot(X, S, color="green", linewidth=1.0, linestyle="-")

subplot(333)
# 轴线(spines)是连接刻度标志和标示数据区域边界的线。它们现在可以被放置在任意地方，它们在子图的边缘。
# 我们将改变这点，因为我们想让它们位于中间。因为一共有四个轴线(上/下/左/右)。我们将通过将它们的颜色设置成None，
# 舍弃位于顶部和右部轴线。然后我们把底部和左部的轴线移动到数据空间坐标中的零点。
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# 让我们在图片左上角添加一个图例。这仅仅需要向plot命令添加关键字参数label(之后将被图例框使用)。
# Plot cosine using blue color with a continuous line of width 1 (pixels)
plot(X, C, color="blue",  linewidth=1.0, linestyle="-.", label="cos")
plot(X, S, color="green", linewidth=1.0, linestyle="-", label="sin")
legend(loc='upper left')#左上

subplot(334)
plot(X, C, color="blue",  linestyle="--")
plot(X, S, color="green", linewidth=1.0, linestyle="-")
# 让我们现在使用annotate命令注解一些我们感兴趣的点。我们选择2π/3作为我们想要注解的正弦和余弦值。
# 我们将在曲线上做一个标记和一个垂直的虚线。然后，使用annotate命令来显示一个箭头和一些文本。
t = 2*np.pi/3
plot([t,t],[0,np.cos(t)], color ='blue', linewidth=2.5, linestyle="--")
# 生成点，50为大小
scatter([t,],[np.cos(t),], 50, color ='blue')
# r就是用LATEX，其用法和L相同
annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
         xy=(t, np.sin(t)), xycoords='data',
         xytext=(+10, +30), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plot([t,t],[0,np.sin(t)], color ='red', linewidth=2.5, linestyle="--")
scatter([t,],[np.sin(t),], 50, color ='red')
annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
         xy=(t, np.cos(t)), xycoords='data',
         xytext=(-90, -50), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# 由于蓝色和红色的线，刻度标签现在很难看清。。我们可以让它们更大
# 并且调整它们的属性使它们的背景半透明。这将让我们把数据和标签都看清。
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))

subplot(335)
n = 12
X = np.arange(n)
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x,y in zip(X,Y1):
    text(x+0.4, y+0.05, '%.2f' % y, ha='center', va= 'bottom')

ylim(-1.25,+1.25)


subplot(336)
def f(x,y): return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)

plt.contourf(X, Y, f(X,Y), 8, alpha=.75, cmap='jet')
C = plt.contour(X, Y, f(X,Y), 8, colors='black', linewidth=.5)
plt.show()
# Show result on screen
show()