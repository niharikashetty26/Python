thisdict = {
    "brand": "Ford",
    "model": "Mustang",

    "year": 2020,
    "year": 1964,
}
print(thisdict)

for i in thisdict:
    print(i)
    print(thisdict[i])

for x in thisdict.values():
    print(x)

for x, y in thisdict.items():
    print(x, y)

del thisdict["brand"]
thisdict["phone"] = "8123758917"
print(thisdict)
print(len(thisdict))
print(type(thisdict))

T = dict(name="John", age=36, country="Norway")
print(T)

T.update({"name": "Niharika"})
print(T)

T.pop("name")
print(T)

T.popitem()
print(T)