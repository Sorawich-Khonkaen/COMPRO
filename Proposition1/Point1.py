def find_multiples_of_three(start: int, end: int) ->list:
        if start > end:
                return[]
        return[num for num in range(start, end)if num % 3 == 0]

print(find_multiples_of_three(10, 25))