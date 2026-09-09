import pandas as pd

df = pd.read_csv("employee.csv")
# print(df)


''' replace empty value with NAN'''
# df.dropna(inplace=True)
# print(df.head(10))

'''replace empty value with 0'''
# df.fillna(inplace=True, value=0)
# print(df.head(10))

'''Filtring'''
# data = df['Designation']=='Manager'
# print(data)
# data = df['Salary']>=40000
# print(data)

'''Sorting'''
# sorted_names=sorted(df['Emp_Name']);
# print(sorted_names)

# reverse_sorted_names=sorted(df['Emp_Name'],reverse=True);
# print(reverse_sorted_names)

'''Grouping'''
# group=df.groupby('Department')
# print(group.get_group("Tech"))


# '''Display Groups Average'''
# Average_salary =df.groupby('Department')['Salary'].mean()
# print("Avg of salary\n",Average_salary)



# '''Display Groups wise count'''
Hr_strength=df.groupby('Department')==['HR'].count()
print("HR empoyees Strength\n",Hr_strength)

# '''Display Groups sum'''
# class_sum=df.groupby('Class')['Marks'].sum()
# print("Class Sum\n",class_sum)