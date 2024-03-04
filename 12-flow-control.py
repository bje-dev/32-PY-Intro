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
