import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
x = range(len(names))
y1 = [0.95, 0.89, 0.94, 0.85, 0.95, 0.94, 0.9, 0.86, 1, 0.88]

plt.plot(x, y1, marker='o', linestyle='-', ms=6, label=u'ConFi')

plt.legend()  # 让图例生效
plt.xticks(x, names, rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"Location")  # X轴标签
plt.ylabel("Accuracy")  # Y轴标签
plt.title("The comparison of spatial attention")  # 标题

plt.show()