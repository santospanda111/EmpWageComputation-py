import random

print("Welcome to Employee Wage Computation Program")
empRatePerHr = 20
empHrs = 8
partTimeHr = 4

'''This condition will check the employee is present or absent.
   According to the presence of employee it'll calculate the salary.
   Added Part time work. 
'''
empOption = random.randint(0, 3)
if empOption == 1:
    print("Employee is Present")
    print(f"Employee's Salary is Rs {empHrs*empRatePerHr}/-")
elif empOption == 2:
    print("Employee is present for Half-Time.")
    print(f"Employee's Salary is Rs {empRatePerHr*partTimeHr}/-")
else:
    print("Employee is Absent")
    print("Employee's Salary is Rs 0/-")
