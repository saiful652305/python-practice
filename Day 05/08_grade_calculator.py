def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"  
p = float(input("Enter your mark: "))
grade = calculate_grade(p)
print(f"{'Your grade is':<16}: {grade}")