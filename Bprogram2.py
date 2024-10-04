def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b


a = int(input("Enter a the 1st number: "))
b = int(input("Enter a the 2nd number: "))

choice = input("Enter the operator (+/-/*//): ")

if choice == '+':
    print(add(a,b))
elif choice == '-':
    print(sub(a,b))
elif choice == '*':
    print(multi(a,b))
elif choice == '/':
    print(div(a,b))
else:
    print("Invalid Input")