def add(val1, val2):
    summ = val1 + val2
    return summ

def subtract(val1, val2):
    subtrr = val1 - val2
    return subtrr

def multiply(val1, val2):
    multt = val1 * val2
    return multt

def divide(val1, val2):
    try:
        divv = val1 / val2
    except ZeroDivisionError:
        return "Division by zero!"
    else:
        return divv

# def root(val1, val2):
#     roott = val1 ** (1 / val2)
#     return roott

def root(val1, val2):
    if val1 > 0:
        roott = val1 ** (1 / val2)
        return roott
    else:
        raise Exception

def power(val1, val2):
    poww = val1 ** val2
    return poww

def percentage(val1, val2):
    percc = val1 * val2 / 100
    return percc


while True:
    try:
        val1 = float(input("Enter val1: "))
    except ValueError:
        print(f'Invalid input, enter some number')
        continue
    s = input("Choose math operation: (+, -, *, **, /, %, 'root'): ")
    if s not in ('+', '-', '*', '**', '/', 'root', '%'):
        continue
    try:
        val2 = float(input("Enter val2: "))
    except ValueError:
        print(f'Invalid input, enter some number')
        continue

    if s == '+':
        print(add(val1, val2))

    elif s == '-':
        print(subtract(val1, val2))

    elif s == '*':
        print(multiply(val1, val2))

    elif s == '/':
        print(divide(val1, val2))

    # elif s == 'root':
    #     print(root(val1, val2))

    elif s == 'root':
        try:
            print(root(val1, val2))
        except:
            print("Impossible to find the root from negative number")

    elif s == '**':
        print(power(val1, val2))

    elif s == '%':
        print(percentage(val1, val2))
