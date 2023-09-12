n1 = int(input())
n2 = int(input())
operator = input()

total = 0
text = ""
if operator == "+":
    total = n1 + n2
    if total % 2 == 0:
        text = "even"
    else:
        text = "odd"
    print(f"{n1} {operator} {n2} = {total} - {text}")

if operator == "-":
    total = n1 - n2
    if total % 2 == 0:
        text = "even"
    else:
        text = "odd"
    print(f"{n1} {operator} {n2} = {total} - {text}")

if operator == "*":
    total = n1 * n2
    if total % 2 == 0:
        text = "even"
    else:
        text = "odd"
    print(f"{n1} {operator} {n2} = {total} - {text}")


if operator == "/" and n2 != 0:
    total = n1 / n2
    print(f"{n1} / {n2} = {total:.2f}")

if operator == "/" and n2 == 0:
    print(f"Cannot divide {n1} by zero")

if operator == "%" and n2 != 0:
    total = n1 % n2
    print(f"{n1} % {n2} = {total}")

if operator == "%" and n2 == 0:
    print(f"Cannot divide {n1} by zero")






