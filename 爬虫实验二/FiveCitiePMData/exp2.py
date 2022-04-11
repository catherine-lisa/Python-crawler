import pandas as pd
import numpy as np
import matplotlib .pyplot as plt

#找出2015年的数据，保存在新的csv文件中
data = pd.read_csv('BeijingPM20100101_20151231.csv', encoding='utf_8_sig')
pd.set_option('display.unicode.east_asian_width', True)

data2015 = data.loc[data['year'] == 2015]
data2015.to_csv("newdata.csv", na_rep='NA')
