# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
x = range(len(names))
plt.xlim(0, 10)  # 限定横轴的范围
plt.ylim(0.7, 1)  # 限定纵轴的范围

y1 = [0.99, 0.98, 0.97, 0.97, 0.98, 0.97, 0.96, 0.99, 0.99, 0.96]
y2 = [0.96, 0.92, 0.98, 0.97, 0.97, 0.97, 0.92, 0.95, 0.97, 0.98]
y3 = [0.93, 0.92, 0.94, 0.81, 0.94, 0.8, 0.82, 0.79, 0.70, 0.86]
# y4 = [1, 0.92, 0.99, 0.97, 0.97, 0.95, 0.99, 0.92, 0.99, 0.93]

plt.plot(x, y1, marker='^', linestyle='-', ms=7, label=u'Sigmoid', color='red')
plt.plot(x, y2, marker='*', ms=7, linestyle='--', label=u'Tanh', color='black')
plt.plot(x, y3, marker='o', ms=6, linestyle='--', label=u'ReLu', color='blue')
# plt.plot(x, y4, marker='o', ms=6, linestyle='--', label=u'SoftMax')
plt.legend(loc='lower left', fontsize=10) # 标签位置

plt.xticks(x, names, rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"Location")  # X轴标签
plt.ylabel("Accuracy")  # Y轴标签
plt.title("The comparison of gate mechanism")  # 标题

ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()