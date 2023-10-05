# Assignment one
def assignment():
    print("Hello world")


assignment()


# Assignment two
def CountingNumbers():
    count = 0
    for i in range(1, 81):
        print(i, end="  ")
        count += 1
        if count == 4:
            count = 0
            print()


CountingNumbers()

# ASSIGNMENT THREE
# Degree Converter from celcius to Fahrenheit
# Enter degrees in celcius
# The temperature in degrees fahrenheit is the


def main():
    converter()


def converter():
    UserInput = float(input("Please input the degrees in celcius: "))

    converter = (UserInput * 9 / 5) + 32

    print(f"The temperature in degrees fahreheit is:{converter} degrees Farenheit")


if __name__ == "__main__":
    main()

# WRITE A FUNCTION THAT RETURNS THE AGE AND THE NAME AS A LIST


def age_name():
    UserDetail = []
    name = str(input("Please input your name: "))
    age = str(input("Please input your age: "))

    UserDetail.append(name)
    UserDetail.append(age)
    print(UserDetail)


age_name()
