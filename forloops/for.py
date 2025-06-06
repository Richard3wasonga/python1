students = ['pascal', 'cristina', 'christopher', 'Brian']

# Loop to print the index and name of each student
for index, student in enumerate(students):
    print(f"Student {index + 1}: {student}")

# Loop to create a list of names with vowels removed
no_vowels = []
vowels = "aeiouAEIOU"
for student in students:
    filtered = ''.join([char for char in student if char not in vowels])
    no_vowels.append(filtered)
print("Names without vowels:", no_vowels)

# Loop to count how many vowels are in each name
vowel_counts = {}
for student in students:
    count = sum(1 for char in student if char in vowels)
    vowel_counts[student] = count
print("Vowel counts per name:", vowel_counts)

# Loop to group names by length
length_groups = {}
for student in students:
    length = len(student)
    if length not in length_groups:
        length_groups[length] = []
    length_groups[length].append(student)
print("Grouped by length:", length_groups)

# Loop to capitalize only the first and last letters of each name
stylized_names = []
for student in students:
    if len(student) > 1:
        stylized = student[0].upper() + student[1:-1] + student[-1].upper()
    else:
        stylized = student.upper()
    stylized_names.append(stylized)
print("Stylized names:", stylized_names)

# Loop to count how many names contain the letter 'r'
r_count = 0
for student in students:
    if 'r' in student.lower():
        r_count += 1
print(f"{r_count} names contain the letter 'r'.")

# Loop to print names in a sorted order
for student in sorted(students, key=lambda x: x.lower()):
    print(f"Sorted name: {student}")

# Loop to build a list of booleans indicating if the name is all lowercase
all_lowercase_flags = []
for student in students:
    all_lowercase_flags.append(student.islower())
print("All lowercase flags:", all_lowercase_flags)
