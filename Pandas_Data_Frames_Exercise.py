import pandas as pd

import producereport

from producereport import produce_dict

produce = (pd.DataFrame(produce_dict, index = ["Cost Per Pound", "Quantity Sold", "Total_Sale"])).T
#print(produce)
#Question1
minimum_sales = produce.Total_Sale.min() #compute min sales
a = (produce['Total_Sale'].sort_values(axis =0 , ascending =False))

print('The product with the highest and lowest sale are')
print(a.iloc[[0, (a.count() - 1)]])
print()

#Question 2
#display total sales of orange and beets
print('The Total sale for orange and beets are: ' ,'\n',(produce.loc[['Orange','Beets'],['Total_Sale']]))

print()

#Question 3

print("The total sales for cucumber is", produce.at['Cucumber', 'Total_Sale'])

#Question 4
filteredpd=(produce[(produce >11500) & (produce<12000)]) #filters value between 11500 and 12000

sortedpd =(filteredpd.sort_values(by= 'Quantity Sold',axis=0 ,ascending=False)) #sorts it in ascending order
index =(sortedpd['Quantity Sold'].count())

print(sortedpd.iloc[0:index,[1]])

print()

#Question 5
print(produce.T)

