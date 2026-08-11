monthly_salary = float(input("Enter your monthly salary: "))
monthly_expenses = float(input("Enter your monthly expenses: "))
monthly_savings = monthly_salary - monthly_expenses
print(f"Your monthly savings are: {monthly_savings}")
annual_salary = monthly_salary * 12
annual_expenses = monthly_expenses * 12
annual_savings = monthly_savings * 12
print(f"Your annual salary is: {annual_salary}")
print(f"Your annual savings are: {annual_savings}")