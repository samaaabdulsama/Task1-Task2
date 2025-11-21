#to install pandas library write in terminal => pip install pandas
import pandas as pd
# From a dictionary
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}
#The DataFrame() function  is one of the most important tools for working with tabular data .
# data arranged in rows and columns, like an Excel spreadsheet or SQL table.
df_dict = pd.DataFrame(data_dict)
print("DataFrame from dictionary:")
print(df_dict)
# From a list of lists
data_list = [
    ['David', 40, 'Tokyo'],
    ['Eve', 28, 'Sydney']
]
df_list = pd.DataFrame(data_list, columns=['Name', 'Age', 'City'])
print("\nDataFrame from list:")
print(df_list)

print("\nDataFrame Info:")
df_list.info()

# Get descriptive statistics such as count , mean (average value) , min , max ,الانحراف المعياري std
print("\nDescriptive Statistics:")
print(df_list.describe())

# Select a single column
print("Age column:")
print(df_dict['Name'])

# Select multiple columns
print("\nName and Age columns:")
print(df_list[['Name', 'Age']])

# Select rows by index label using .loc
print("\nRow with index 1 (using .loc):")
print(df_dict.loc[1])

# Select rows by integer position using .iloc
print("\nRow with position 0 (using .iloc):")
print(df_list.iloc[0])
