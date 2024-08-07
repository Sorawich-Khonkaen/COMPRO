numbers = [4, 2, 9, 1, 5, 6]

length = len(numbers)
print(f"Length of the list: {length}")

total_sum = sum(numbers)
print(f"Sum of all elements: {total_sum}")

max_value = max(numbers)
print(f"Maximum vale: {max_value}")

min_value = min(numbers)
print(f"Minimum value: {min_value}")

sorted_numbers = sorted(numbers)
print(f"Sorted list: {sorted_numbers}")

bool_list = [False, True, False]
any_true = any(bool_list)
print(f"Is any element True? {any_true}")

all_true = all(bool_list)
print(f"Are all elements True? {all_true}")

string = "hello"
char_list = list(string)
print(f"List of characters: {char_list}")

reversed_numbers = list(reversed(numbers))
print(f"Reversed list: {reversed_numbers}")

enumerate_numbers = list(enumerate(numbers))
print(f"Enumerated list: {enumerate_numbers}")