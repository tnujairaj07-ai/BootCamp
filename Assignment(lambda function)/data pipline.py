from functools import reduce

nums = list(range(1, 11))
odd_nums = list(filter(lambda x: x % 2 != 0, nums))
squared = list(map(lambda x: x * x, odd_nums))
result = reduce(lambda a, b: a + b, squared)
print("odd_nums", odd_nums)
print("Squared=", squared)
print("sum=", result)

# Mini calculator
def make_operator(op):
    if op == "+":
        return lambda a, b: a + b
    elif op == "-":
        return lambda a, b: a - b
    elif op == "*":
        return lambda a, b: a * b
    elif op == "/":
        return lambda a, b: a / b
    elif op == "%":
        return lambda a, b: a % b
    elif op == "**":
        return lambda a, b: a ** b
    else:
        return lambda a, b: "Invalid Operator"