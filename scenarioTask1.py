hat = [1, 2, 3, 4, 5]

# step one to replace the middlenumber

NewNumber = input("please input a new number: ")

hat[2] = NewNumber

print(hat)

# step two is to remove the last digit in the array
del hat[-1]

print(hat)

# step three is to check the length of the array

print(len(hat))
