# SCENARIO TWO

#  Step one Creating a list named beatles

beatles = []

# Adding Elements to the list

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")


print(beatles)

print("Enter the names Stu Stucliffe, Pete Best:")
for i in range(2):
    user_input = input()
    beatles.append(user_input)
print(beatles)

del beatles[4]
del beatles[3]

print(beatles)

beatles.insert(0, "Ringo Starr")

print(beatles)
