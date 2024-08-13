student = {"name": "Alice", "age": 25, "grade": "A", "major": "Computer Science"}
for key in student:
    print(f"{key}: {student[key]}")

print("----------------------------------")

student = {"name": "Alice", "age": 25, "grade": "A", "major": "Computer Science"}
for value in student.values():
    print(value)

print("----------------------------------")

student = {"name": "Alice", "age": 25, "grade": "A", "major": "Computer Science"}
for key, value in student.items():
    print(f"{key}: {value}")