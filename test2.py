# _*_ coding: utf-8 _*_
# 导入忽视警告模块
import warnings
warnings.filterwarnings('ignore')
# 导入需要的包，并读取表格特定列,并按照时间降序排列
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#处理数据：读取，分组，合并
def read_excel():
    df = pd.read_excel("huawei_XHS.xlsx", usecols = [3, 4, 5, 10]).sort_values(by='笔记发布时间', ascending=True)
    print(df)

