#matplotlib合并
# _*_ coding: utf-8 _*_

'''
NumPy 通常与 SciPy（Scientific Python）和 Matplotlib（绘图库）一起使用， 这种组合广泛用于替代 MatLab，是一个强大的科学计算环境，有助于我们通过 Python 学习数据科学或者机器学习。
'''

import matplotlib.pyplot as plt    # 导入matplotlib包

figure = plt.figure()             # 创建一个figure画布
axes1 = figure.add_subplot(2,1,1)         # 获取每个axes1的位置
axes2 = figure.add_subplot(2,1,2)         # 获取每个axes2的位置

axes1.plot([1,3,5,7],[4,6,15,3])                   # 获取axes1的坐标
axes2.plot([12,8,6,4],[1,10,2,0])                  # 获取axes2的坐标

figure.show()   # pycharm中绘图的话，必须加这句代码才能显示。而notebook可以不用加这句代码，自动显示

