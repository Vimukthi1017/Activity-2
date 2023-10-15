# header
print("Income Details")

# basic salary, allowances, and deductions
basic_salary = float(input("Enter basic salary: $"))
allowances = float(input("Enter allowances: $"))
deductions = float(input("Enter deductions: $"))

# Calculate gross salary
gross_salary = basic_salary + allowances

# Calculate net salary
net_salary = gross_salary - deductions

# Display the calculated net salary
print("\nNet Salary: $", net_salary)
