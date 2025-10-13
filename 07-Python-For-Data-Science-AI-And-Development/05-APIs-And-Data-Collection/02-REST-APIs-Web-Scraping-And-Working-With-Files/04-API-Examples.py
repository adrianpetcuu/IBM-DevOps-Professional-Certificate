from randomuser import RandomUser
import pandas as pd

r = RandomUser()
some_list = r.generate_users(10)
print(some_list)

name = r.get_full_name()

for user in some_list:
    print(user.get_full_name(), " ", user.get_email())

# EXAMPLE 1
for user in some_list:
    print(user.get_picture())

# generate a table with information about the users
def get_users():
    users = []
    for user in RandomUser.generate_users(10):
        users.append({"Name": user.get_full_name(), "Gender": user.get_gender(),
                      "City": user.get_city(), "State": user.get_state(),
                      "Email": user.get_email(), "DOB": user.get_dob(), "Picture": user.get_picture()})
    return pd.DataFrame(users)

print(get_users())

df1 = pd.DataFrame(get_users())

# EXAMPLE 2
import requests
import json
data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")
results = json.loads(data.text)
print(pd.DataFrame(results))

# 'nutrition' column contains multiple subcolumns
df2 = pd.json_normalize(results)
print(df2)

cherry = df2.loc[df2["name"] == "Cherry"]
print((cherry.iloc[0]['family']), (cherry.iloc[0]['genus']))

cal_banana = df2.loc[df2["name"] == 'Banana']
print(cal_banana.iloc[0]['nutritions.calories'])

# EXERCISE 3
data2 = requests.get("https://official-joke-api.appspot.com/jokes/ten")

results2 = json.loads(data2.text)

df3 = pd.DataFrame(results2)
df3.drop(columns=["type", "id"], inplace=True)
print(df3)