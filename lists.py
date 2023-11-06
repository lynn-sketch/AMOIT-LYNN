numbers = [10, 8, 9, 2, 1]
names = []

print(names)

print(numbers[2])

# how to know the length of the list
print(len(numbers))

# swapping elements in the list
numbers[2] = 90
print(numbers)

# deleting numbers in the list
del numbers[0]
print(numbers)

# printing numbers from the back side
print(numbers[-2])

# Functions

# result = function(arg)

result = len(numbers)
print(result)


# result = data.method(arg)

# ADDING ELEMENTS ON A LIST USING METHODS

numbers.append(4)
print(numbers)

# inserting an element on a list
numbers.insert(0, 202)
numbers.insert(2, 500)

print(numbers)


# declaring an empty list
my_list = []

for i in range(100):
    my_list.append(i + 1)
print(my_list)

my_list.insert(0, "startcounting")
print(my_list)


# BUBBLE SORT
# It helps us swap and arrange elements in a list in ascending order

my_list = [
    8,
    9,
    30,
    2,
    1,
    7,
]

# # -1 is to make sure we start counting from 1
# for i in range(len(my_list) - 1):
#     # comparing elements close to each other which is greater
#     if my_list[i] > my_list[i + 1]:
#         # Here we are swapping indexes if one is greater than the other
#         my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print(my_list)

# my_list = []

# swapped = True

# num = int(input("How many elements do you want to input:"))

# for i in range(num):
#     val = int(input("enter a list of elements:"))
#     my_list.append(val)

# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         # -1 is to make sure we start counting from 1
#         # comparing elements close to each other which is greater
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#         # Here we are swapping indexes if one is greater than the other
#         my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

#     print("sorted:")
#     print(my_list)

# Reversing elements we use a method
# my_list.reverse

# SLICING USING METHODS

list = [1, 9, 8, 7, 10]

# copying tghe entire list with a limit such as start from index 1 to index 3
list_2 = list[1:3]

list_3 = list[2:4]

print(list_2)
print(list_3)

# we can also delete elements in a list


# IN AND NOT

# it returns booleans true or false
list = [1, 9, 8, 7, 10]
print(5 not in list)
print(9 in list)

# getting the largest number in last

list = [1, 9, 8, 7, 10]
largest = list[0]

for i in list:
    if i > largest:
        largest = i
print(largest)
