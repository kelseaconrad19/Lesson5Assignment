# Task 1: Code a function to calculate the average grade.
def calculate_grade(grade_list):
    add_list = sum(grade_list)
    average = add_list / len(grade_list)
    return average
# Task 2: Implement a function to find the highest and lowest grade.


def high_low(grade_list):
    lowest = min(grade_list)
    highest = max(grade_list)
    return lowest, highest


# Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).
def categorize_grades(grade_list):
    categorized_grades = []
    for x in grade_list:
        if 90 <= x <= 100:
            grade = "A"
        elif 80 <= x <= 89:
            grade = "B"
        elif 70 <= x <= 79:
            grade = "C"
        elif 60 <= x <= 69:
            grade = "D"
        else:
            grade = "F"
        categorized_grades.append(grade)
    categorized_grades.sort()
    return categorized_grades


grades_list = [100, 92, 87, 65, 74, 23, 87]
print(categorize_grades(grades_list))

