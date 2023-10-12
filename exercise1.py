numbers = []
sum = 0
count = 0
while True:
    # ALLOWING THE USER ENTER THEIR OWN NUMBERS
    try:
        number = input("Please input any number: ")
        numbers.append(number)
        if number == "done":
            break
        else:
            number = float(number)
            sum += number
            count += 1
    except ValueError:
        print("please input a digit")

average = sum / count
print(f"Sum = {sum}")
print(f"Count = {count}")
print(f"Average = {average}")
# else:
#     print("Lynn")

#     finally:
#         print("Goodluck")


# # REMOVING THE LAST USER INPUT
# del numbers[-1]

# # TURNING NUMBERS INTO INTEGERS
# numbers = [int(i) for i in numbers]
# sum = 0
# for j in range(len(numbers)):
#     sum += numbers[j]
# print(f"Total = {sum}")

# length = len(numbers)

# print(f"Count is {length}")

# Average = sum / length

# print(f"Average is {Average}")
