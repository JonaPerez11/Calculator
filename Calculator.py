def switch_op(choice,num1,num2):
    switcher = {
        1: add(num1, num2),
        2: sub(num1, num2),
        3: mult(num1, num2),
        4: div(num1, num2)
    }
    return switcher.get(choice)

def add(num1, num2):
    return num1+num2

def sub(num1, num2):
    return num1-num2

def mult(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2

def main():
    print("Please press the number for the operation you would like to perform: ")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    choice = int(input("Operation: "))
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(switch_op(choice,num1,num2))



main()