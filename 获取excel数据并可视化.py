# _*_ coding: utf-8 _*_
#导入忽视警告模块
import warnings
warnings.filterwarnings('ignore')

#导入三个包
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#读取excel文件
df = pd.read_excel("huawei_XHS.xlsx")
#df

#dict.values():返回在给定字典(也就是df）中的所有可用的值的列表
for data in df.values:
    print(data,type(data))  #此处打印type需要加“（）”
    



# print(df.values)
# print(type(df))


#显示中文字符
plt.rcParams['font.sans-serif'] = ['SimHei']

#选择特定列绘图
df.plot(x='笔记发布时间', y='笔记评论量', kind='pie')
plt.show()
