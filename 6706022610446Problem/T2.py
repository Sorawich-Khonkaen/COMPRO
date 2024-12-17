money = int(input("Enter Money: "))
if money <= 1000 :
    i = 0.1
elif money <= 10000 :
    i = 0.05
else:
    i = 0.02
M = money +(money*i)
print('ดอกเบี้ยพร้อมเงินต้น:',M)