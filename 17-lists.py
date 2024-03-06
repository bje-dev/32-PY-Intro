number = [1, 2, 3]
print(number)

leters = ["a", "b", "c"]
print(leters)

words = ["Hello", "My ", "Name", "Is"]
print(words)

booleans = [True, False, True, False]
print(booleans)

matriz = [[0, 1], [1, 0]]
print(matriz)

zero = [0] * 10
print(zero)

alf = number + leters
print(alf)

ran = list(range(1, 11))
print(ran)

chars = list("Bucketbot")
print(chars)

# LIST EDIT

cars = ["Blue", "Red", "Yellow", "Black"]
print(cars)
cars[0] = "Green"
print(cars)
print(cars[0:3])
print(cars[2:])
print(cars[-1])
print(cars[1::2])

numbers = list(range(21))
print(numbers[1::2])

# UNPACK LISTS

numbers = [1, 2, 3]

# first=numbers[0]
# second=numbers[1]
# third=numbers[2]

first, second, third = numbers
print(first, second, third)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
one, two, *group, last = num
print(one, last, group)

# ITERATION AND TUPLES

dogs = ["Zorro", "Atila", "Pulga", "Pirata"]

for index, dog in enumerate(dogs):
    print(index, dog)

# SEARCH ELEMENT IN LIST
print(dogs.count("Pulga"))

if "Pulga" in dogs:
    print(dogs.index("Pulga"))

# EDIT LISTS

os = ["Mac", "Win", "Deb", "Ubu"]
os.insert(1, "Fed")
os.append("Min")
print(os)

os.remove("Win")
os.pop(1)
del os[0]
os.clear()
print(os)

# SORT LISTS

ratings = [2, 4, 1, 15, 44, 66]
ratings.sort()  # SEE SORTED
print(ratings)
ratings.sort(reverse=True)
print(ratings)


users = [[4, "Nicolas"], [1, "Javier"], [3, "Bernardo"], [6, "Sebastian"]]
users.sort()
print(users)

# LAMBDA FUNCTION

users.sort(key=lambda el: el[1], reverse=True)
print(users)

# COMPREHENSION

names = []
for user in users:
    names.append(user[0])
print(names)


names = [user[0] for user in users]
print(names)

# TUPLES

numtuple = (1, 2, 3) + (4, 5, 6)
print(numtuple)

point = tuple([1, 2])
print(point)

# ACCESS TO TUPLE

somenumbers = numtuple[:2]
print(somenumbers)

# UNPACK TUPLE
first, second, *others = numtuple
print(first, second, others)

for n in numtuple:
    print(n)

# NOTE: TUPLES CANNOT BE MODIFIED