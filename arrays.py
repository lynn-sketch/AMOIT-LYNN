num1 = 5
num2 = 3
num3 = 8
num4 = 2
num5 = 7

total = num1 + num2 + num3 + num4 + num5

print(f"THE TOTAL IS {total}")


numbers = [5, 3, 8, 2, 7]
total = 0
for num in numbers:
    total += num
print(f"the total is :{total}")


stack_example = []

stack_example.append("one")
stack_example.append("two")
stack_example.append("three")
stack_example.append("four")

print("initial stack with four elements one to four")
print(stack_example)

print("elements removed from stack in order")
print(stack_example.pop())
print(stack_example.pop())
print(stack_example.pop())

print("stack after three elements are popped")
print(stack_example)
print("stack has remained with one element")

print(stack_example.pop())
print(stack_example)
print("stack is now empty please add some more values to it")

stack_example.append("1, 2, 3, 4, 5")
stack_example.append("6, 7, 8, 9, 10")
print(stack_example)
print(stack_example.pop())
print(stack_example)
