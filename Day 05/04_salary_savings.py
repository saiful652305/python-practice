monthly_salary = int(input("Enter your monthly salary: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
savings = monthly_salary - monthly_expenses
print(f"\n\n{'Monthly saving':<16}: {savings}")
annual_salary = monthly_salary * 12
annual_expenses = monthly_expenses * 12
print(f"{'Annual salary':<16}: {annual_salary}")
print(f"{'Annual expense':<16}: {annual_expenses}")
annual_savings = annual_salary - annual_expenses
print(f"{'Annual saving':<16}: {annual_savings}")
saving_rate = (annual_savings / annual_salary) * 100
print(f"{'Saving rate':<16}: {saving_rate:.2f}%")