import pandas as pd
df=pd.read_csv('StudentData.csv')


''' replace empty value with NAN'''
# df.dropna(inplace=True)
# print(df.head(10))

'''replace empty value with 0'''
# df.fillna(inplace=True, value=0)
# print(df.head(10))

'''Filtring'''
# data = df['Class']=='TYCS'
# print(data)
# data = df['Marks']>=59
# print(data)

'''Sorting'''
# sorted_names=sorted(df['Name']);
# print(sorted_names)

# reverse_sorted_names=sorted(df['Name'],reverse=True);
# print(reverse_sorted_names)

'''Grouping'''
# group=df.groupby('Class')
# print(group.get_group("TYCS"))


'''Display Groups Average'''
class_average=df.groupby('Class')['Marks'].mean()
print("Avg of class\n",class_average)



'''Display Groups maximum'''
class_maximum=df.groupby('Class')['Marks'].max()
print("Class Maximum\n",class_maximum)

'''Display Groups minimum'''
class_minimum=df.groupby('Class')['Marks'].min()
print("Class Minimum\n",class_minimum)

'''Display Groups wise count'''
class_strength=df.groupby('Class')['Marks'].count()
print("Class Strength\n",class_strength)

'''Display Groups sum'''
class_sum=df.groupby('Class')['Marks'].sum()
print("Class Sum\n",class_sum)