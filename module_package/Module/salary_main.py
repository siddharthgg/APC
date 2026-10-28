# main.py

from salary import gross_salary, deductions, net_salary

name = input("Enter employee name: ")

basic = float(input("Enter basic salary: "))
hra = float(input("Enter HRA: "))
da = float(input("Enter DA: "))

gross = gross_salary(basic, hra, da)
deduction = deductions(gross)
net = net_salary(gross, deduction)

print("\n----- Employee Salary Details -----")
print("Employee Name:", name)
print("Gross Salary:", gross)
print("Total Deductions:", deduction)
print("Net Salary:", net)