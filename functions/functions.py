def cube(number):
    return number**3


print(cube(9))

# DATA STRUCTURES
# -Data
# -operations
# -lists[]
# -tuples()
# -dictionaries{}
# -sets{}


def add_n_sub(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    return [addition, subtraction]


print(add_n_sub(90, 50))

print(type(add_n_sub(9, 8)))


def main():
    print(name())
    print(hall())


def name():
    name = input("what is your name: ")
    return name


def hall():
    hall = input("what is your hall: ")
    return hall


print(main())


def main():
    add(20, 90)
    multiply(100, 900)

    def add(a, b):
        print("The sum is =", a + b)

    def multiply(a, b):
        print("The product is =", a * b)

    def diff(a, b):
        print("The diff is =", a - b)

    def quotient(a, b):
        print("The quotient is =", a / b)

    print(main())
