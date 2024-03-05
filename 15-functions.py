# parameters and arguments
def hello():
    print("Hello function!")


def printername(name, surname):
    print(f"Hello {name} {surname}")


def sume(a, b, c):
    print(a, b, c)


def iterable(*numbers):  # SINGLE ASTERISK
    result = 0
    for number in numbers:
        result += number
        print(result)


def get_product(**data):  # DOUBLE ASTERISK - SEE KWARGS (KEYWORD ARGS)
    print(data["id"], data["name"])


def multiplication(a, b):
    total = a * b
    return total


hello()
printername("Bernardo", "Espinoza")
# NAMED ARGUMENTS
printername(name="Bernardo", surname="Espinoza")
# XARGS
sume(2, 5, 7)
# ITERABLE
iterable(5)
# KWARGS
get_product(id="84", name="nokia", desc="This is a nokia")
# RETURN FUNCTION
ret = multiplication(2, 3)
print(ret)
