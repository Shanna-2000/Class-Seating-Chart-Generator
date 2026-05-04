import sys

# Prompt for user inputs

file_path = input("Enter the file path: ")
groups = int(input("Enter the number of groups: "))
group_sizes = [0] * groups
for i in range(groups):
    group_sizes[i] = int(input(f"Enter size for group {i+1}: "))

# Read the file and process
try:
    with open(file_path, 'r') as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f"File {file_path} not found.")
    sys.exit(1)

count = 0
students = []
male = 0
female = 0

for line in lines:
    parts = line.strip().split()
    if len(parts) == 2:
        try:
            num = int(parts[0])
            gender = parts[1].lower()
            if gender in ['m', 'f']:
                students.append((num, gender))
                count += 1
                if gender == 'm':
                    male += 1
                if gender == 'f':
                    female += 1
        except ValueError:
            continue  # Skip invalid lines

print(f"Total numbers followed by 'm' or 'f': {count}")
print(f"Students: {students}")  # Optional: to show stored data
print(f"Male students: {male}")
print(f"Female students: {female}")