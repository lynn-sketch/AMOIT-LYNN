# number two
def evaluate_prefix(expression):
    stack = []
    operators = ["+", "-", "*", "/"]
    expression = expression.split()

    for token in reversed(expression):
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            operand1 = stack.pop()
            operand2 = stack.pop()
            result = perform_operation(token, operand1, operand2)
            stack.append(result)

    return stack.pop()


def evaluate_postfix(expression):
    stack = []
    operators = ["+", "-", "*", "/"]

    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(token, operand1, operand2)
            stack.append(result)

    return stack.pop()


def perform_operation(operator, operand1, operand2):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2


prefix_expression = "* + 5 4 7"
postfix_expression = "5 4 + 7 *"

prefix_result = evaluate_prefix(prefix_expression)
postfix_result = evaluate_postfix(postfix_expression)

print("Prefix expression result:", prefix_result)
print("Postfix expression result:", postfix_result)
