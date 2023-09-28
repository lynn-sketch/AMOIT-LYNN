x = 0
for i in range(0, 100):
    x += i

    size = 12
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            print(f"{str(i*j):>4}")


lst = [14, 8, -23, 4, 6, 10, -18, 5, 5, 11]
maxSum = lst[0]
for i in range(0, len(lst)):
    for j in range(i, len(lst)):
        sumz = 0
        for s in range(j, len(lst)):
            sumz += lst[s]
        if sumz > maxSum:
            maxSum = sumz
        print("maximum suv Array sum = ", maxSum)
