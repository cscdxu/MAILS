# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
x = range(len(names))
plt.xlim(0, 10)  # 限定横轴的范围
plt.ylim(0.7, 1)  # 限定纵轴的范围

y1 = [0.99, 0.99,    0.97, 0.86, 0.99, 0.97, 0.95, 0.95, 0.97, 0.93]
y2 = [0.99, 0.95, 0.97, 0.94, 0.98, 0.93, 0.93, 0.9,  0.98, 0.98]
y3 = [0.99, 0.98, 0.97, 0.97, 0.98, 0.97, 0.96, 0.99, 0.99, 0.96]

plt.plot(x, y1, marker='o', ms=6, linestyle='--', label=u'GAP', color='blue')
plt.plot(x, y2, marker='*', ms=7, linestyle='--', label=u'GMP', color='black')
plt.plot(x, y3, marker='^', ms=7, linestyle='-', label=u'GHP', color='red')

plt.legend(loc='lower left', fontsize=12) # 标签位置
plt.xticks(x, names, rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"Location")  # X轴标签
plt.ylabel("Accuracy")  # Y轴标签
plt.title("The comparison of channel attention")  # 标题

ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()