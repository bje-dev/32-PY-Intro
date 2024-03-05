############# IF ############
age = 22

if age > 54:
    print("Old person")
elif age > 17:
    print("Young person")
else:
    print("Unfit person")

# ANOTHER EXAMPLE WITH A SINGLE PRINT

if age > 54:
    message = "Old person"
elif age > 17:
    message = "Young person"
else:
    message = "Unfit person"

print(message)

########### IF TERNARY ##########

message = "Old person" if age > 54 else "Young person"
print(message)

############## FOR ##############

for age in range(5):
    print(age)

############ FOR ELSE ############
search = 3
for age in range(5):
    if age == search:
        print("Found", search)
        break
else:
    print("Age not found")

############ ITERABLE ############

#Iterable : range(5)
#Lists
#Tuples

for char in "Python code":
    print(char)

######### NESTED LOOP ############

# outer loop - inner loop
for j in range(3):
    for k in range(2):
        print(f"{j}, {k}")

############# WHILE ##############

numberwhile = 1

while numberwhile < 100:
    print(numberwhile)
    numberwhile *= 2

command = ""
while command.lower() != "exit":
    command = input("$ ")
    print(command)





