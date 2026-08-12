def calculate_age(birth_year, current_year):
    return current_year - birth_year
b_year = int(input("Enter your birth year: "))
c_year = int(input("Enter the current year: "))
age = calculate_age(b_year, c_year)
print(f"Your age is approximately {age} years.")