while True:
    s = int(input("Enter numberstart: "))
    e = int(input("Enter numberend: "))
    d = int(input("Enter Dividend: "))
    for i in range(s,e ):   
        if i % d == 0:
            print(i)

    sum = int(input("Exit Press 0,Continue Press 1: "))
    if sum == 0:
            break
        
        