# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(6,10), dpi=800)
X1 = np.arange(1,9,1)
# plt.suptitle("", fontsize=30)
#------------------------------第一个----------------------------------------
plt.subplot(311)
plt.xlim(0.5, 8.5)
plt.ylim(0, 0.6)
plt.subplots_adjust(hspace=0.3, wspace=0.9)
plt.grid()
plt.title('Delay percent on PageRank')

Y1 = [0.05, 0.09, 0.13, 0.17, 0.25, 0.33, 0.41, 0.5]
Y2 = [0.049, 0.051, 0.053, 0.055, 0.12, 0.17, 0.22, 0.25]

plt.plot(X1, Y1, linewidth=2.0, color="blue", label="PageRank-P")
plt.plot(X1, Y2, linewidth=2.0, color="red", label="PageRank-S")

plt.ylabel('$T_{delay}$')
plt.xlabel(r'$Ratio$')
plt.legend(loc='upper left')

for i in X1:
    plt.scatter([i,],[Y1[i-1],], 50, color ='blue')
    plt.scatter([i,],[Y2[i-1],], 50, color ='red')

#------------------------------第二个----------------------------------------
plt.subplot(312)
plt.xlim(0.5, 8.5)
plt.ylim(0, 0.4)
# plt.subplots_adjust(bottom=0.15)
plt.grid()
plt.title('Delay percent on WordCount')

Y1 = [0.05, 0.07, 0.09, 0.11, 0.14, 0.185, 0.23, 0.28]
Y2 = [0.049, 0.051, 0.053, 0.055, 0.095, 0.125, 0.155, 0.19]

plt.plot(X1, Y1, linewidth=2.0, color="blue", label="WorkCount-P")
plt.plot(X1, Y2, linewidth=2.0, color="red", label="WorkCount-S")

plt.ylabel(r'$T_{delay}$')
plt.xlabel(r'$Ratio$')
plt.legend(loc='upper left')

for i in X1:
    plt.scatter([i,],[Y1[i-1],], 50, color ='blue')
    plt.scatter([i,],[Y2[i-1],], 50, color ='red')

#------------------------------第三个----------------------------------------
plt.subplot(313)
plt.xlim(0.5, 8.5)
plt.ylim(0, 0.2)
# plt.subplots_adjust(bottom=0.15)
plt.grid()
plt.title('Delay percent on WordCount')

Y1 = [0.05, 0.055, 0.065, 0.075, 0.1, 0.117, 0.134, 0.152]
Y2 = [0.05, 0.057, 0.07, 0.08, 0.11, 0.13, 0.152, 0.172]


plt.plot(X1, Y1, linewidth=2.0, color="blue", label="Kmeans-P")
plt.plot(X1, Y2, linewidth=2.0, color="red", label="Kmeans-S")

plt.ylabel(r'$T_{delay}$')
plt.xlabel(r'$Ratio$')
plt.legend(loc='upper left')

for i in X1:
    plt.scatter([i,],[Y1[i-1],], 50, color ='blue')
    plt.scatter([i,],[Y2[i-1],], 50, color ='red')
plt.savefig("test.jpg")
# plt.show()

