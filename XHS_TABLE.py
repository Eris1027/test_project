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

    # .to_datetime( '笔记发布时间', format='%Y-%m-%d')
    # df.groupby('笔记发布时间').groups
    grouped = df.groupby(by=['笔记发布时间'])['笔记点赞量','笔记评论量','笔记收藏量'].sum()

    # print(grouped)

    grouped.to_excel("group_merge_demo.xlsx",index=True)
    print("saved successfully")
    return grouped

# 绘图
def drawing():
    # 读取上一步骤返回的数据
    df = pd.read_excel('group_merge_demo.xlsx')
    for data in df.values: # dict.values():返回在给定字典(也就是df）中的所有可用的值的列表
        print(data)  # 此处打印type需要加“（）”

    plt.figure(figsize=(10,7))  # 设置画布的尺寸
    plt.title('转评赞总量', fontsize=14)  # 标题，并设定字号大小
    plt.xlabel(u'笔记发布时间', fontsize=14)  # 设置x轴，并设定字号大小
    plt.ylabel(u'数量', fontsize=14)  # 设置y轴，并设定字号大小
    # 设置三条折线参数
    total_width, n = 0.8, 3  # 有多少个类型，只需更改n即可
    width = total_width / n
    x_label = df['笔记发布时间'].astype(str).apply(lambda x: x[:10]).tolist()


    plt.bar(np.arange(df.shape[0]), df['笔记点赞量'], width=width, color="#2b2e4a", label='笔记点赞量')
    plt.bar(np.arange(df.shape[0])+width, df['笔记评论量'], width=width, color="#e84545", label='笔记评论量', tick_label=x_label)
    plt.bar(np.arange(df.shape[0])+width*2, df['笔记收藏量'], width=width, color="#903749", label='笔记收藏量')
    plt.legend(loc="upper left")
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(3))

    # df['笔记发布时间']
    # 显示中文字符
    plt.rcParams['font.sans-serif'] = ['SimHei']

    # # 选择特定列绘图
    # df.plot(x='笔记发布时间', y='笔记评论量', kind='bar')
    plt.show()


if __name__ == '__main__':
    drawing()