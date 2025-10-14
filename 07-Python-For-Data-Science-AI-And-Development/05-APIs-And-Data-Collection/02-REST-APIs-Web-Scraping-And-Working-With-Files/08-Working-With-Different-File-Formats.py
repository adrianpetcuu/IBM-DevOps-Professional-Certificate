# CSV FILE
import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"

df = pd.read_csv(filename)
print(df)

df.columns = ['First Name', 'Last Name', 'Location', 'City', 'State', 'Area Code']
print(df)

print(df["First Name"])

df = df[['First Name', 'Last Name', 'Location', 'City', 'State', 'Area Code']]
print(df)

# to select the first row
print(df.loc[0])

# to select the 0th, 1st and 2nd row of "First Name" column only
print(df.loc[[0, 1, 2], "First Name"])

# to select the 0th, 1st, 2nd row of "First Name" column only
print(df.iloc[[0, 1, 2], 0])

# import library
import pandas as pd
import numpy as np

# create a dataframe
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
print(df)

# applying the transform function
df = df.transform(func = lambda x : x + 10)
print(df)

result = df.transform(func = ['sqrt'])
print(result)

# JSON FILE
import json

person = {
    'first_name': 'Mark',
    'last_name': 'abc',
    'age': 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

with open('person.json', 'w') as f: # writing JSON object
    json.dump(person, f)

# Serializing json
json_object = json.dumps(person, indent=4)
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

print(json_object)

# Deserialization
# Opening JSON file
with open('sample.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

print(json_object)
print(type(json_object))

# XLSX FILE
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx"
df = pd.read_excel(filename)
print(df)


# XML FILE
import xml.etree.ElementTree as ET

# create the file structure
employee = ET.Element('employee')
details = ET.SubElement(employee, 'details')
first = ET.SubElement(details, 'firstname')
second = ET.SubElement(details, 'lastname')
third = ET.SubElement(details, 'age')
first.text = 'Shiv'
second.text = 'Mishra'
third.text = '23'
# create a new XML file witth the results
mydata1 = ET.ElementTree(employee)
# myfile = open("items2.xml", "wb")
# myfile.write(mydata)
with open("new_sample.xml", "wb") as files:
    mydata1.write(files)

# ---------- Descărcare fișier XML (înlocuiește !wget) ----------
import requests
from io import BytesIO
import xml.etree.ElementTree as ET
from pathlib import Path
xml_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Sample-employee-XML-file.xml"
r = requests.get(xml_url, timeout=30)
r.raise_for_status()
dest = Path("Sample-employee-XML-file.xml")
dest.write_bytes(r.content)
print(f"Am salvat: {dest.resolve()}")

# Parse the XML file
tree = ET.parse("Sample-employee-XML-file.xml")
# Get the root of the XML tree
root = tree.getroot()
# Define the columns for the DaraFrame
columns = ["firstname", "lastname", "title", "division", "building", "room"]
# Initialize an empty DataFrame
dataframe = pd.DataFrame(columns=columns)
# Iterate through each node in the XML root
for node in root:
    # Extract text from each element
    firstname = node.find("firstname").text
    lastname = node.find("lastname").text
    title = node.find("title").text
    division = node.find("division").text
    building = node.find("building").text
    room = node.find("room").text
    # Create a DataFrame for the current row
    row_df = pd.DataFrame([[firstname, lastname, title, division, building, room]], columns=columns)
    # Concatenate with the existing DataFrame
    dataframe = pd.concat([dataframe, row_df], ignore_index=True)

print(dataframe)

# reading xml file using pandas.read_xml function
# Herein xpath we mention the set of xml nodes to be considered for migrating  to the dataframe which in this case is details node under employees.
df = pd.read_xml("Sample-employee-XML-file.xml", xpath="/employees/details")
# save data
dataframe.to_csv("employee.csv", index=False)

# BINARY FILE FORMAT
# Reading the Image file
# import PIL
from PIL import Image
import urllib.request
urllib.request.urlretrieve("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg", "dog.jpg")

# read image
img = Image.open('./dog.jpg', 'r')
# output images
img.show()


# DATA ANALYSIS
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"
df = pd.read_csv(filename)
# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe")
print(df.head(5))
print(df.shape)
# statistical overview of dataset
print(df.info())
print(df.describe())

# identify and handle missing values
missing_data = df.isnull()
print(missing_data.head())

# count missing values in each column
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")

# correct data format
print(df.dtypes)

# visualization
import matplotlib.pyplot as plt
import seaborn as sns

labels = 'Not Diabetic', 'Diabetic'
plt.pie(df['Outcome'].value_counts(), labels=labels, autopct='%0.02f%%')
plt.legend()
plt.show()