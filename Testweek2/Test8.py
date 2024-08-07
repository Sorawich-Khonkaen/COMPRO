scores1 = int(input("Get the first test score: "))
scores2 = int(input("Get the second test score: "))
scores3 = int(input("Get the third test score: "))

sum = (scores1 + scores2) + scores3
print("Display the average: ", sum)
if sum > 95:
    print('Display"congratulations!"')