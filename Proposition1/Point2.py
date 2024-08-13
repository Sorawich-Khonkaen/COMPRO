def find_multiples_of_three_and_four(start: int,end: int)->list:
    if start > end:
        return[]
    return[num for num in range(start, end)if num % 3 == 0 and num % 4 == 0]

print(find_multiples_of_three_and_four(10, 50))