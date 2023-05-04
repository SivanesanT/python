"""
20.dictionary & its function.py
in here keys and values c0me
"""
user={
    "name":"ram",
    "age":25,
    "is married":True
}
print(user)
print(type(user))
print(user["name"])
# reduvatti ore keyword kudutha oree tha than eduthukkum
print(user.get("age"))
print(user.keys())
print(user.values())
print(user.items())
for x in user:
    print(x)

for x in user.values():
    print(x)

for x in user.keys():
    print(x)

for x,y in user.items():
    print(x, " ",y)

if "age" in user:
    print("present")

if "gender" in user:
    print("present")
#changing values

user.update({"gender" : "male"})
print(user)
user["age"]=35
print(user)
user.pop("age")
print(user)
user.clear()
print(user)
# del means all are deleted



























#nesteddictionery

users = {
    "user1": {
        "name": "ram",
        "age": 25,
        "is married": True
    },
    "user2": {
        "name": "sam",
        "age": 35,
        "is married": False
    }
}
print(users)


