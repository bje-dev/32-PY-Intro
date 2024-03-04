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

########### TERNARY ##########

message = "Old person" if age > 54 else "Young person"
print(message)
