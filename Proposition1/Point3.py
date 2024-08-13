def find_non_multiples(start: int,end: int)->list:
    if start > end:
        return[]
    return[num for num in range(start, end)if num % 3 != 0 and num % 4 != 0 and num % 5 != 0]

print(find_non_multiples(10, 25))
    