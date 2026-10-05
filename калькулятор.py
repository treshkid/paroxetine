a = float(input("Первое число: "))
op = input("Операция (+ - * /): ")
b = float(input("Второе число: "))

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Неверная операция")
