mydictionary = {"a": "onion", "b": "tomatoe", "c": "carrots"}

len(mydictionary)


# length of my dictionary
print(len(mydictionary))

# retrieving data from a dictionary
print(mydictionary["a"])

# adding a new item to the dictionary
mydictionary["d"] = "pineapple"
print(mydictionary)


# deleting from my dictionary
del mydictionary["b"]
print(mydictionary)


if "c" in mydictionary:
    print("c is a key in my dictionary")

# for key in mydictionary:
#     print(key, mydictionary(key))


# students = {}
# def add_student(name,email,grade):
#     if name not in students:
#     student[name] = {"email": email, "grade": {}}
# student[name]["grade"][subject] = grade


# TUPLES

# Creating a tuple in python

rgb = (255, 0, 0)


days = ("Monday", "Tuesday", "Wednesday", "Thurday", "Friday", "Saturday", "Sunday")

# printing the first days excluding the fifth index
print(days[:5])


# copying everything from a tuple
week_days = days[:]
print(week_days)


# Adding tuples together
new = days + week_days
print(new)

# Sorting tuples
# Printing numbers in ascending order

numbers = (2, 8, 9, 1, 4, 1, 5)
print(sorted(numbers))

# Printing the number of times one appears
print(numbers.count(1))


# printing numbers in decsending order
numbers = (2, 8, 9, 1, 4, 1, 5)
print(sorted(numbers, reverse=True))
