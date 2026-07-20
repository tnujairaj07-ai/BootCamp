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

# Testing
add = make_operator("+")
subtract = make_operator("-")
multiply = make_operator("*")
divide = make_operator("/")
modulo= make_operator("%")
exponential=make_operator("**")
a, b = 20, 5

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))
print("Modulo:", modulo(a, b))
print("Exponent", exponential(a, b))