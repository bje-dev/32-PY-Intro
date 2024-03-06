# SET MEANS A GROUP OF DATA

first = {1, 1, 2, 2, 3, 3, 4, 4}
print(first)
first.add(5)
first.remove(1)
print(first)

second = [3, 4, 5]
second = set(second)

print(first | second) #IT COMPLETES THE MISSING NUMBERS BETWEEN THE FIRST AND THE SECOND GROUP
print(first & second) #IT PRINTES THE INTERSECTION BETWEEN THE FIRS AND THE SECOND GROUP
print(first - second) # IT PRINTES THE DIFERENCE BETWEEN THE FIRST AND THE SECOND GROUP
print(first ^ second) # IT PRINTES THE SIMETRIC DIFRENCE BETWEEN THE FIRST AND THE SECOND GROUP
