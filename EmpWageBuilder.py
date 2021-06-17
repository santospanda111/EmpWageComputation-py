import random

from Emp_wage_Interface import EmpInterface
from CompanyEmpWage import CompanyEmpWage


class EmpWageBuilder(EmpInterface):
    """
    -Here i have implemented the abstract methods of Emp_interface class.
    """

    company_list = []

    def add_company(self, company_name, max_hr_per_month, total_days, wage_per_hr):
        """
        -This method will add company details by object of CompanyEmpWage.
        -Append the data to company_list.
        :param company_name:
        :param max_hr_per_month:
        :param total_days:
        :param wage_per_hr:
        :return:
        """
        employee_info = CompanyEmpWage(company_name, max_hr_per_month, total_days, wage_per_hr)
        self.company_list.append(employee_info)
        return employee_info

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

    def calculate_monthly_wage(self, employee_info):
        """
        -this one is an instance method where i have called checkAttendance method to get workHours.
        -calculate monthly wage.
        -Here i have added a condition (Calculate monthly wage till 100 hrs and 20 days)
        :return: monthly_wage
        """
        monthly_wage = 0
        emp_hours = 0
        day = 1
        while (emp_hours < employee_info.max_hr_per_month) and (day < employee_info.total_days):
            self.check_attendance()
            emp_hours = emp_hours + self.work_hour
            daily_wage = employee_info.wage_per_hr * self.work_hour
            print(f"Employee daily Wage is : {daily_wage}")
            monthly_wage = monthly_wage + daily_wage
            day = day + 1
        print(f"Company name is {employee_info.company_name}\nEmployee hours : {emp_hours} and Days : {day}")
        if emp_hours > 100:
            monthly_wage -= daily_wage
            emp_hours -= self.work_hour
            print(f"Employee hours : {emp_hours} and Days : {day}")
        print(f"\nEmployee's Salary for the Entire Month is: {monthly_wage}\n")