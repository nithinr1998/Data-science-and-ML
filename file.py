
import pandas as py
df = py.read_csv('sales_data.csv')
print(df.head())
row,column=df.shape

print("No of Rows is:",row)
print("No of Column is :",column)

revenuesum=df['Revenue'].sum()
print("Revenue Sum is :",revenuesum)
