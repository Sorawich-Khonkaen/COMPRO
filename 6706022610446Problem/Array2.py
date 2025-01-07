import array as arr
a = arr.array('i', [50, 87, 65, 39])
print ("Print All data in array : ", end =" ")
for i in range (0, 4):
    print (a[i], end =" ")
print()
max1 = max(a)
min1 = min(a)
print("Max :",max1,"Min :",min1)
number = sum(a)
average = sum(a)/len(a)
print("Sum :",number,"Average :",average)
a = sorted( a )
print("Sort min to max and print :",a)
a.sort(reverse=True)
print("Sort max to min and print :",a)

odd = []
even = []


for i in a:
    if i % 2 == 0:
        print("Show odd number :",i)

for i in a:
    if i % 2 != 0:
        print("Show even number :",i)


    