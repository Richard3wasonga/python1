students = ['pascal', 'cristina','christopher','Brian']

# Loop to print each name in uppercase
for student in students:
    print(student.upper())

# Loop to check if the name starts with a specific letter
for student in students:
    if student.lower().startswith('c'):
        print(f"{student} starts with the letter C.")

# Loop to count how many students have names longer than 6 characters
long_name_count = 0
for student in students:
    if len(student) > 6:
        long_name_count += 1
print(f"{long_name_count} students have names longer than 6 letters.")

# Loop to create a dictionary with names and their lengths
name_lengths = {}
for student in students:
    name_lengths[student] = len(student)
print(name_lengths)

# Loop to pair each student with a greeting message
messages = []
for student in students:
    messages.append(f"Hi {student.title()}, welcome to the class!")
print(messages)

# Nested loop to print each character in each student’s name
for student in students:
    print(f"Characters in {student}:")
    for char in student:
        print(f"  - {char}")

# Loop with conditional formatting based on name length
for student in students:
    if len(student) <= 6:
        print(f"{student} has a short name.")
    elif len(student) <= 8:
        print(f"{student} has a medium name.")
    else:
        print(f"{student} has a long name.")

# Loop to create a list of students' names in reverse order (not just reversed list)
reversed_names = []
for student in students:
    reversed_names.append(student[::-1])
print("Reversed names:", reversed_names)
