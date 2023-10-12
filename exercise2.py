# ENTERING CLIENT DETAILS


name = input("Please input your name: ")
amount = input("Please input the amount you got: ")
amount = int(amount)
days_spent = input("Enter days taken with the loan: ")
days_spent = int(days_spent)


if days_spent <= 30:
    Total = (amount * 10 / 100) + amount
    print(f"The total loan to be paid is {Total}")

if days_spent > 30:
    Total = (amount * 10 / 100) + (amount) + (amount * 1 / 100)
    print(f"The total loan to be paid is {Total}")
