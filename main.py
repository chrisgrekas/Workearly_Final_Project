import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('finance_liquor_sales2016_2019.csv')
groupedf=df.groupby(['zip_code','item_description'])['bottles_sold'].sum()
mpi=groupedf.groupby('zip_code').idxmax() #mpi=most popular items
sbs=df.groupby('store_name')['sale_dollars'].sum()#sbs=sales by store
total_sales=sbs.sum()
sales_percentage=(sbs/total_sales)*100
result=df.groupby('zip_code')['bottles_sold'].sum()
plt.scatter(result.index,result.values)
plt.xlabel('Zip Code')
plt.ylabel('Bottles sold')
plt.show()
