# _*_ coding: utf-8 _*_
#导入忽视警告模块
import warnings
warnings.filterwarnings('ignore')

#导入包
import pandas as pd

#读取excel文件
df = pd.read_excel("huawei_XHS.xlsx")
df.head()
