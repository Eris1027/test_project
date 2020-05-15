#合并报表AB

import pandas as pd    # step1：导入 pandas 模块，简称pd

name_a = "表A.xlsx"    #step2：获取需要合并的表格名称A，注意要加格式后缀
# print(table_a)

name_b = "表B.xlsx"  #step2：获取需要合并的表格名称A，注意要加格式后缀
# print(table_b)


a = pd.read_excel(name_a)  #step3：pandas（简称pd） 通过 read_excel（）  方法来读取表格内容
b = pd.read_excel(name_b)   #step3：pandas（简称pd） 通过 read_excel（）  方法来读取表格内容
# print(type(a),type(b))
result = pd.concat([a,b])   #step4：pandas（简称pd） 通过concat([列表]) 方法来合并表A和表B
# print(result)

result.reset_index(drop=True,inplace=True)   #step5： 调整序号：drop=True删除旧的index，inplace=True替换成新index
result["序号"] = range(1, len(result)+1)
# print(result)

result.to_excel("result_v3.xlsx",index=True)   #step6： 将合并后的数据通过 to_excel 方法保存到 xlsx 表格中
print("successful")

