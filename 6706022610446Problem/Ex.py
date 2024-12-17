print("***calculate sum of odd and even number (Exit prss 0)***")

odd = 0
even = 0

while True:
    sum = int(input("Enter number: "))
    num = int(sum)
    if sum == 0:
       break
    elif num % 2 == 0:
         even += num

    elif num % 2 != 0:
        odd += num

print(f"sum of even number: {even}")      
print(f"sum of odd number: {odd}")       
 
