import random

print("Welcome to Employee Wage Computation Program")
empRatePerHr = 20
empHrs = 8
'''This condition will check the employee is present or absent.
   According to the presence of employee it'll calculate the salary. 
'''
empOption = random.randint(0, 2)
if empOption == 1:
    print("Employee is Present")
    print(f"Employee's Salary is Rs {empHrs*empRatePerHr}/-")
else:
    print("Employee is Absent")
    print("Employee's Salary is Rs 0/-")
