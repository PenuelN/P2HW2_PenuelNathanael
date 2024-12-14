# Nathanael Penuel
# 10/13/2024
# P2HW2
# Take grades in and calculate


# Input grades
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

# Store grades in a list
grades = [grade1, grade2, grade3, grade4, grade5, grade6]

# Calculate grades
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average = sum_of_grades / len(grades)

# Output results
print("\n------------Results------------")
print(f"{'Lowest Grade:':<20} {lowest_grade:.1f}")
print(f"{'Highest Grade:':<20} {highest_grade:.1f}")
print(f"{'Sum of Grades:':<20} {sum_of_grades:.1f}")
print(f"{'Average:':<20} {average:.2f}")
print("--------------------------------")
