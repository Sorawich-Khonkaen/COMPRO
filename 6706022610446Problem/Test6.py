print("***Calculate the sum between start and stop number***")
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
sum = 0
for i in range(start,end +1):
    sum += i    
print(f"The sum from {start} to {end} is: {sum}")
