students = ['pascal', 'cristina','christopher','Brian']

for student in students:
    print(student)

for student in students:
    print(f"Hello, {student.title()}!")

for student in students:
    print(f"{student} has {len(student)} letters.")

for index, student in enumerate(students):
    print(f"{index + 1}. {student}")

for student in students:
    if len(student) > 7:
        print(f"{student} has a long name.")

formatted_names = []

for student in students:
    formatted_names.append(student.capitalize())

print(formatted_names)

for student in reversed(students):
    print(student)
