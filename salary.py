import sys

# Get values from Jenkins command
name = sys.argv[1]
basic_salary = float(sys.argv[2])

# Calculate HRA and DA
hra = basic_salary * 20 / 100
da = basic_salary * 10 / 100

gross_salary = basic_salary + hra + da

# Display output
print("Employee Salary Details")
print("-----------------------")
print("Employee Name:", name)
print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("DA:", da)
print("Gross Salary:", gross_salary)