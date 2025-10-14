from bs4 import BeautifulSoup # this module helps in web scrapping
import requests # this module helps us to download a web page

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())

# tags
tag_object = soup.title
print("tag object: ", tag_object)
print("tag object type: ", type(tag_object))

tag_object = soup.h3
print(tag_object)

# children, parents, and siblings
tag_child = tag_object.b
print(tag_child)

parent_tag = tag_child.parent
print(parent_tag)

print(tag_object)

print(tag_object.parent)

sibling_1 = tag_object.next_sibling
print(sibling_1)

sibling_2 = sibling_1.next_sibling
print(sibling_2)

sibling_3 = sibling_2.next_sibling
print(sibling_3)

# HTML Attributes
print(tag_child['id'])
print(tag_child.attrs)
print(tag_child.get('id'))

# Navigable String
tag_string = tag_child.string
print(tag_string)
print(type(tag_string))
unicode_string = str(tag_string)
print(unicode_string)

# Filters
table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, 'html.parser')
# find_all(name, attrs, recursive, string, limit, **kwargs)
table_rows = table_bs.find_all('tr')
print(table_rows)
first_row = table_rows[0]
print(first_row)
print(type(first_row))
print(first_row.td)

for i, row in enumerate(table_rows):
    print("row", i, "is", row)

for i, row in enumerate(table_rows):
    print("row", i)
    cells = row.find_all('td')
    for j, cell in enumerate(cells):
        print('column', j, "cell", cell)

list_input = table_bs.find_all(name=["tr", "td"])
print(list_input)

# Attributes
print(table_bs.find_all(id="flight"))

list_input = table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
print(list_input)

print(table_bs.find_all(href=True))

# EXERCISES
# Find all the `<a>` tags without 'href' value
print(table_bs.find_all(lambda tag: tag.name == "a" and not tag.has_attr("href")))

# Find all the elements that do not contain any links
print(table_bs.find_all(lambda tag: tag.name != "a" and not tag.find('a')))

# Using the soup object soup, find the element with the id attribute content set to "boldest"
print(soup.find_all(id="boldest"))

# string
# With string you can search for strings instead of tags, where we find all the elments with Florida
print(table_bs.find_all(string="Florida"))

# we store the HTML as a Python string and assign two_tables
two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"
# we create a BeautifulSoup object two_tables_bs
two_tables_bs = BeautifulSoup(two_tables, 'html.parser')
# we can find the first table using the tag name table
print(two_tables_bs.find("table"))
# we can filter on the class attribute to find the second table, but because class is a keyword in Python
# we add an underscore to differentiate them
print(two_tables_bs.find("table", class_='pizza'))

# DOWNLOADING AND SCRAPING THE CONTENTS OF A WEB PAGE
url = "http://www.ibm.com"
data = requests.get(url).text
soup = BeautifulSoup(data, "html.parser") # create a soup object using the variable 'data'
for link in soup.find_all('a', href=True): # in html anchor/link is represented by the tag <a>
    print(link.get('href'))

# Scrape all images Tags
for link in soup.find_all('img'): # in html page image is represented by the tag <img>
    print(link)
    print(link.get('src'))

# Scrape data from HTML tables
#The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

# get the contents of the webpage in text format ad store in a variable called data
data = requests.get(url).text

soup = BeautifulSoup(data,"html.parser")

# find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>

# Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    print("{}--->{}".format(color_name, color_code))