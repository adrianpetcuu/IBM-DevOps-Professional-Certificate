# Import required library
import pandas as pd

# Read data from CSV file
csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv'
df = pd.read_csv(csv_path)

print(df.head())

# Access to the column Length
x = df[['Quantity']]
print(x)

# Viewing Data and Accessing Data
# Get the column as a series
x = df['Product']
print(x)

# Get the column as a dataframe
x = df[['Quantity']]
print(x)

# Access to multiple columns
y = df[['Product', 'Category', 'Quantity']]
print(y)

# Access the value on the first row and the first column
print(df.iloc[0, 0])

# Access the value on the second row and the first column
print(df.iloc[1, 0])

# Access the value on the first row and the third column
print(df.iloc[0, 2])

# Access the value on the second row and the third column
print(df.iloc[1, 2])

# Access the column using the name
print(df.loc[0, 'Product'])

# Access the column using the name
print(df.loc[1, 'Product'])

# Access the column using the name
print(df.loc[1, 'CustomerCity'])

# Access the column using the name
print(df.loc[1, 'Total'])

# Slicing the dataframe
print(df.iloc[0:2, 0:3])

# Slicing the dataframe using name
print(df.loc[0:2, 'OrderID':'Category'])

# Use a variable q to store the column Price as a dataframe
q = df[['Price']]
print(q)

# Assign the variable q to the dataframe that is made up of the column Product and Category
q = df[['Product', 'Category']]
print(q)

# Access the 2nd row and the 3rd column of df
print(df.iloc[1, 2])

# Use the following list to convert the dataframe index df to characters and assign it to df_new;
# Find the element corresponding to the row index a and column 'CustomerCity'
# Then select the rows a through d for the column 'CustomerCity'
new_index = ['a', 'b', 'c', 'd', 'e']
df_new = df
df_new.index = new_index
print(df_new.loc['a', 'CustomerCity'])
print(df_new.loc['a':'d', 'CustomerCity'])
