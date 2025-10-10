# Let's us import the Pandas Library
import pandas as pd

# Define a dictionary 'x'
x = {
    'Name': ['Rose', 'John', 'Jane', 'Mary'],
    'ID': [1, 2, 3, 4],
    'Department': ['Arhitect Group', 'Software Group', 'Design Team', 'Infrastructure'],
    'Salary': [100000, 80000, 50000, 60000]
}

# Casting the dictionary yo a DataFrame
df = pd.DataFrame(x)

# Display the result df
print(df)

# Retrieving the "ID" column and assigning it to a variable x
x = df[['ID']]
print(x)

# Check the type of x
print(type(x))

# Retrieving the Deparment, Salary and ID columns and assigning it to a variable z
z = df[['Department', 'Salary', 'ID']]
print(z)

# Create DataFrame
a = {
    'Student': ['David', 'Samuel', 'Terry', 'Evan'],
    'Age': ['27', '24', '22', '32'],
    'Country': ['UK', 'Canada', 'China', 'USA'],
    'Course': ['Python', 'Data Structures', 'Machine Learning', 'Web Development'],
    'Marks': ['85', '72', '89', '76']}
df1 = pd.DataFrame(a)
print(df1)

# Assign Marks column to variable b
b = df1[['Marks']]
print(b)

# Retrieve the Country and Course columns and assign it to a variable c
c = df1[['Country', 'Course']]
print(c)

# To view the columns as a series, just use one bracket
# Get the Student Column as a series Object
x = df1['Student']
print(x)

# Check the type of x
print(type(x))

# Access the value on the first row and the first column
print(df.iloc[0, 0])

# Access the value on the first row and the third column
print(df.iloc[0, 2])

# Access the column using the name
print(df.loc[0, 'Salary'])

df2 = df
df2 = df2.set_index("Name")

# To display the first 5 rows of new dataframe
print(df2.head())

# Now, let us access the column using the name
print(df2.loc['Jane', 'Salary'])

# Use the loc() fucntion to get the Department of Jane
print(df2.loc['Jane', 'Department'])

# Use the iloc() function to get the Salary of Mary in the newly created dataframe df2
print(df2.iloc[3, 2])

# Let's us do the slicing using old dataframe df
print(df.iloc[0:2, 0:3])

# Let's us do the slicing using loc() function on old dataframe df where index column is having labels as 0, 1, 2
print(df.loc[0:2, 'ID':'Department'])

# Let's us do te slicing using loc() function on new dataframe df2 where index column is Name having labels:
# Rose, John and Jane
print(df2.loc['Rose': 'Jane', 'ID': 'Department'])

# Using loc() function, do slicing an old dataframe df to retrieve the Name, ID and Department
# Of index having labels as 2, 3
print(df.loc[2:3, 'Name':'Department'])