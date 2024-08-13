def calculate_sum_and_average()->None:
    numbers = []
    for i in range(5):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    total_sum = sum(numbers)
    average = total_sum / len(numbers)

    print(f"The sum is: {total_sum:.2f}")
    print(f"The average is: {average:.2f}")

calculate_sum_and_average()