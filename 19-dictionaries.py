point = {"x": 25, "y": 50}  # KEYS SHOULD BE A STRING

print(point["x"])
point["z"] = 45
print(point)

if "y" in point:
    print("Found")

if "c" in point:
    print("Not found")

print(point.get("x"))
print(point.get("b", 99))

del point["x"]
del (point["y"])

print(point)
point[""] = 22

for value in point:
    print(value, point[value])

for key, value in point.items():
    print(key, value)

# REAL EXAMPLE

users = [
    {"id": 1, "name": "Bernardo"},
    {"id": 2, "name": "Julian"},
    {"id": 2, "name": "Espinoza"},
]

for user in users:
    print(user["name"])

list1 = [1, 2, 3, 4]
list2 = [5, 6]

join = ["Hello", *list1, "My", *list2, "Name"]
print(join)

point1 ={"x": 19}
point2 ={"y": 15}

newpoint = {**point1, **point2}
print(newpoint)
