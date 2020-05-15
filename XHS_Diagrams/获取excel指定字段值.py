# _*_ coding: utf-8 _*_
#导入忽视警告模块
import warnings
warnings.filterwarnings('ignore')

#导入需要的包，并读取表格特定列,并按照时间降序排列
import pandas as pd
import numpy as np
df = pd.read_excel("huawei_XHS.xlsx", usecols = [3, 4, 5, 10]).sort_values(by='笔记发布时间', ascending=True)


# .to_datetime( '笔记发布时间', format='%Y-%m-%d')
# df.groupby('笔记发布时间').groups
grouped = df.groupby(by=['笔记发布时间'])['笔记点赞量','笔记评论量','笔记收藏量'].sum()

print(grouped)

# grouped.to_excel("group_merge_demo.xlsx",index=True)
print("saved successfully!!")
