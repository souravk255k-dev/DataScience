import pandas as pd

# s = pd.Series([10, 20, 30, 40])
# print("Pandas Series s:")
# print(s)

# data1 = {'name': ['Alice', 'Bob'], 'Age': [25, 30]}
# df1 = pd.DataFrame(data1)
# print(df1)

# data2 = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
#     'score': [85, 90, 78, 92, 88, 75]
# }
# df2 = pd.DataFrame(data2)

# print(df2.head())        
# print(df2.head(3))       

# df2.info()               

# print(df2.describe())    
# print(df2.columns)       
# print(df2.shape)

data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New york', 'Los angeles',None]
}
df = pd.DataFrame(data, index=['a', 'b', 'c'])

print(df.loc['a'])                  
print(df.loc['b', 'name'])         
print(df.loc[:, ['name', 'city']])

print(df.iloc[0])
print(df.iloc[1,0])
print(df.iloc[:,0:2])

print(df.isnull())
print(df.dropna()) 
print(df.filena(0))

print(df['age'].filena(df['age'].mean(),inplace=True))
print(df)
