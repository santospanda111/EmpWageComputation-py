import random


class Emp_wage_builder:
    company_list = []

    def __init__(self, *company):
        """
        -Here i have used *args to take multiple arguments.
        -According to that i have taken multiple objects and while initializing i have added all the elements in the list.
        :param company:
        """
        self.company_list.extend(company)

    def check_attendance(self):
        """
        -This method will get the workHour according to the attendance which will generate random numbers.
        :return:workHour
        """
        attendance = (random.randint(0, 2))
        if attendance == 1:
            print('Employee is present full time')
            self.work_hour = 8
        elif attendance == 2:
            print('Employee is present part time')
            self.work_hour = 4
        else:
            print('Employee is absent')
            self.work_hour = 0
        return self.work_hour

    def calculate_monthly_wage(self, company):
        """
        -this one is an instance method where i have called checkAttendance method to get workHours.
        -calculate monthly wage.
        -Here i have added a condition (Calculate monthly wage till 100 hrs and 20 days)
        :return: monthly_wage
        """
        monthly_wage = 0
        emp_hours = 0
        day = 1
        while (emp_hours < company.max_hr_per_month) and (day < company.total_days):
            self.check_attendance()
            emp_hours = emp_hours + self.work_hour
            daily_wage = company.wage_per_hr * self.work_hour
            print(f"Employee daily Wage is : {daily_wage}")
            monthly_wage = monthly_wage + daily_wage
            day = day + 1
        print(f"Company name is {company.company_name}\nEmployee hours : {emp_hours} and Days : {day}")
        if emp_hours > 100:
            monthly_wage -= daily_wage
            emp_hours -= self.work_hour
            print(f"Employee hours : {emp_hours} and Days : {day}")
        print(f"\nEmployee's Salary for the Entire Month is: {monthly_wage}\n")

    def company_emp_wage(self):
        """
        -This method will iterate and get each object and call calculate_monthly_wage.
        """
        for company in self.company_list:
            self.calculate_monthly_wage(company)
