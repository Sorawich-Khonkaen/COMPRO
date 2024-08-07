boy = int(input("Number of boy: "))
girl = int(input("Number of girl: "))

boy = boy/(boy+girl) * 100
girl = girl/(boy+girl)* 100
print("Total number of boys",boy,'%')
print("Total number of girls",girl,'%')