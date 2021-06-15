import random

print("Welcome to Employee Wage Computation Program")
# This condition will check the employee is present or absent.
empOption = random.randint(0, 2)
if empOption == 1:
    print("Employee is Present")
else:
    print("Employee is Absent")
