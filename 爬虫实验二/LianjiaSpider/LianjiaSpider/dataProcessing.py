import pandas as pd
import numpy as np
import matplotlib .pyplot as plt

data = pd.read_csv('data.csv', encoding='utf_8_sig')
pd.set_option('display.unicode.east_asian_width', True)

#找出总价最贵和最便宜的房子，以及总价的中位数
max_tot_price = pd.DataFrame.max(data["tot_price"])
min_tot_price = pd.DataFrame.min(data["tot_price"])
median_tot_price = pd.DataFrame.median(data["tot_price"])
print("for total price of houses:")
print("highest price:", max_tot_price)
print("lowest price:", min_tot_price)
print("median price:", median_tot_price)

#找出均价最贵和最便宜的房子，以及单价的中位数
max_avg_price = pd.DataFrame.max(data["avg_price"])
min_avg_price = pd.DataFrame.min(data["avg_price"])
median_avg_price = pd.DataFrame.median(data["avg_price"])
print("for average price of houses:")
print("highest price:", max_avg_price)
print("lowest price:", min_avg_price)
print("median price:", int(median_avg_price))

#找到总价在均值三倍标准差以外的房屋
standard_deviation = pd.DataFrame.std(data["tot_price"])
print(standard_deviation)

#列出总价在均值三倍标准差以外的房屋
standard = 3 * standard_deviation
a = data.loc[data['tot_price'] > standard]
print("Outliers of standard deviation:")
print(a)

#通过箱型图原则判断并列出均价为异常值的房屋
plt.boxplot(x=data['avg_price'])
plt.show()
q1 = data['avg_price'].quantile(q=0.25)
q3 = data['avg_price'].quantile(q=0.75)
q2 = data['avg_price'].quantile(q=0.5)
low_limit = q1 - 1.5 * (q3-q1)
high_limit = q3 + 1.5 * (q3-q1)
print(q1,q2,q3,low_limit,high_limit)
val = data.loc[(data['avg_price'] > high_limit)|(data['avg_price'] < low_limit)]
print("Outliers of box plot: ")
print(val)

#离散化处理
#bins = [0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
bins = [0,20000,40000,60000,90000]
cuts = pd.cut(data['avg_price'], bins)
print(pd.value_counts(cuts))
print(pd.value_counts(cuts, normalize=True))