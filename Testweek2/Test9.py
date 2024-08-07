print("Select operations form 1.(+), 2.(-), 3.(*), 4(/)")
operations = int(input("Select: "))

if operations <=4 and operations > 0:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if operations == 1:
        print(f"{num1}+ {num2} = {(num1)+(num2)}")
    elif operations == 2:
        print(f"{num1}-{num2} = {(num1)-(num2)}")
    elif operations == 3:
        print(f"{num1}*{num2} = {(num1)*(num2)}")
    elif operations == 4:
        print(f"{num1}/{num2} = {(num1)/(num2)}")
else :
    print("invalid operations select")