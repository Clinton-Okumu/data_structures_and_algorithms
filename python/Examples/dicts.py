#  A `dict` (short for *dictionary*) is a **mutable**, **unordered** collection of **key-value** pairs. Keys must be **unique** and **immutable**.

# usng curly braces
user = {"id": 1, "name": "clint okumu"}

# accessing values
user["id"]
user["name"]

# accessing keys
user.keys()
user.values()
user.items()

# adding
user["age"] = 30
print(user)

# removing
del user["age"]
print(user)

# iterating
for key, value in user.items():
    print(f"{key}: {value}")

for key in user:
    print(key, user[key])
