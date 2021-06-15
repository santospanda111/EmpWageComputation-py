import random

print("Welcome to Employee Wage Computation Program")
empRatePerHr = 20
empHrs = 8
partTimeHr = 4

'''
Added a function which will get the employee hrs.
according to that it'll print that employee is present or absent. 
'''
empOption = random.randint(0, 2)


def workingHrs(empOption):
    switcher = {
        0: 0,
        1: empHrs,
        2: partTimeHr
    }
    working_Hr = switcher.get(empOption)
    if working_Hr == 8:
        print("Employee is Present")
    elif working_Hr == 4:
        print("Employee is Present for Half-Time")
    else:
        print("Employee is Absent")
    return working_Hr

'''
this method will calculate the salary and return that.
'''
def computeSalary(empRatePerHr, working_Hr):
    return empRatePerHr * working_Hr
print(f"Employee Salary is Rs {computeSalary(empRatePerHr, workingHrs(empOption))}/-")