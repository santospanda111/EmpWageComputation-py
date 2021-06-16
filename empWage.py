import random


class Employee_wage:
    emp_daily_wage = 0
    wage_Per_Hour = 20
    work_hour = 0
    daily_wage = 0
    is_absent = 0
    is_fulltime = 1
    is_part_time = 2
    full_time_hours = 8
    part_time_hours = 4

    def __init__(self, company_name, max_hr_per_month, total_days, wage_per_hr):
        self.company_name = company_name
        self.max_hr_per_month = max_hr_per_month
        self.total_days = total_days
        self.wage_per_hr = wage_per_hr

    @staticmethod
    def check_attendance():
        """
        -This method will get the workHour according to the attendance which will generate random numbers.
        :return:workHour
        """
        attendance = (random.randint(0, 2))
        if attendance == 1:
            print('Employee is present full time')
            Employee_wage.work_hour = 8
        elif attendance == 2:
            print('Employee is present part time')
            Employee_wage.work_hour = 4
        else:
            print('Employee is absent')
            Employee_wage.work_hour = 0
        return Employee_wage.work_hour

    def calculate_monthly_wage(self):
        """
        -this one is an instance method where i have called checkAttendance method to get workHours.
        -calculate monthly wage.
        -Here i have added a condition (Calculate monthly wage till 100 hrs and 20 days)
        :return: monthly_wage
        """
        monthly_wage = 0
        emp_hours = 0
        day = 1
        while (emp_hours < self.max_hr_per_month) and (day < self.total_days):
            Employee_wage.check_attendance()
            emp_hours = emp_hours + Employee_wage.work_hour
            daily_wage = self.wage_per_hr * Employee_wage.work_hour
            print(f"Employee daily Wage is : {daily_wage}")
            monthly_wage = monthly_wage + daily_wage
            day = day + 1
        print(f"Company name is {self.company_name}\nEmployee hours : {emp_hours} and Days : {day}")
        if emp_hours > 100:
            monthly_wage -= daily_wage
            emp_hours -= Employee_wage.work_hour
            print(f"Employee hours : {emp_hours} and Days : {day}")
        print(f"\nEmployee's Salary for the Entire Month is: {monthly_wage}")


if __name__ == '__main__':
    print('Welcome to Employee Wage Computation Program')
    bridgelabz = Employee_wage("Bridgelabz", 100, 20, 20)
    print(bridgelabz.calculate_monthly_wage())
    amazon = Employee_wage("Amazon", 100, 20, 15)
    print(amazon.calculate_monthly_wage())
