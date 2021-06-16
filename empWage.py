import random
class EmployeeWage:
    wage_Per_Hour = 20
    workHour = 0
    dailyWage = 0
    isAbsent = 0
    isFullTime = 1
    isPartTime = 2
    fullTimeHours = 8
    partTimeHours = 4

    def checkAttendance(cls):
        """
        -This method will get the workHour according to the attendance which will generate random numbers.
        :return:workHour
        """
        attendance = (random.randint(0, 2))
        if attendance == 1:
            print('Employee is present full time')
            EmployeeWage.workHour = 8
        elif attendance == 2:
            print('Employee is present part time')
            EmployeeWage.workHour = 4
        else:
            print('Employee is absent')
            EmployeeWage.workHour = 0
        return EmployeeWage.workHour

    def calculateMonthlyWage(self):
        """
        -this one is an instance method where i have called checkAttendance method to get workHours.
        -calculate monthly wage.
        :return: monthlyWage
        """
        monthlyWage = 0
        for day in range(1, 21):
            EmployeeWage.checkAttendance(self)
            dailyWage = EmployeeWage.wage_Per_Hour * EmployeeWage.workHour
            print(f"Employee daily Wage is : {dailyWage}")
            monthlyWage = monthlyWage + dailyWage
        else:
            print("Employes's monthly salary", monthlyWage)


if __name__ == '__main__':
    print('Welcome to Employee Wage Computation Program')
    emp = EmployeeWage()
    print(emp.calculateMonthlyWage())