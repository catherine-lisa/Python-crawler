import pandas as pd
import numpy as np
import matplotlib .pyplot as plt

data = pd.read_csv('newdata.csv', encoding='utf_8_sig')
pd.set_option('display.unicode.east_asian_width', True)

#找出空值：对新的csv文件，找出存在的空值列及相应的空值数量
#方法一
print(data.shape)
print(data.count(axis=0))
print([data.shape[0]] - data.count(axis=0))
emptylines = [data.shape[0]] - data.count(axis=0)
#方法二
for item in data.columns:
    print(item, data[item].isnull().sum())


#对所有存在空值的列，给出空值的处理方法及理由，要求处理方法必须可在本数据集范围内执行
#东四环空值较多，填充数据则不准确，选择删去该列
newdata = data.drop(columns="PM_Dongsihuan")

#对于其他含空的数据，使用前面一个值进行填充
newdata = newdata.fillna(method="ffill")

#输出成新的csv文件
newdata.to_csv("finalresult.csv")
print([data.shape[0]] - newdata.count(axis=0))