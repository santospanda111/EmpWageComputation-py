import random

from Emp_wage_Interface import EmpInterface
from CompanyEmpWage import CompanyEmpWage
from EmpWageException import EmpWageException
import json

class EmpWageBuilder(EmpInterface):
    """
    -Here i have implemented the abstract methods of Emp_interface class.
    """
    company_list = []
    company_dict = dict()

    def __init__(self):
        self.work_hour = 0

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
        try:
            employee_info = CompanyEmpWage(company_name, max_hr_per_month, total_days, wage_per_hr)
            self.company_list.append(employee_info)
            if len(self.company_list) == 0:
                raise EmpWageException(' List is empty ')
            return employee_info
        except Exception as e:
            print("Invalid", e)

    def check_attendance(self, attendance):
        """
        -This method will get the workHour according to the attendance which will generate random numbers.
        :return:workHour
        """
        try:
            switcher = {
                0: 0,
                1: 8,
                2: 4
            }
            return switcher.get(attendance, 0)
        except Exception as e:
            print("Invalid", e)

    def calculate_monthly_wage(self, employee_info):
        """
        -this one is an instance method where i have called checkAttendance method to get workHours.
        -calculate monthly wage.
        -Here i have added a condition (Calculate monthly wage till 100 hrs and 20 days)
        :return: monthly_wage
        """
        work_hour = 0
        daily_wage = 0
        monthly_wage = 0
        emp_hours = 0
        day = 1
        count_days = 0
        try:
            while (emp_hours < employee_info.max_hr_per_month) and (day < employee_info.total_days):
                count_days += 1
                attendance = (random.randint(0, 2))
                work_hour = self.check_attendance(attendance)
                emp_hours = emp_hours + work_hour
                daily_wage = employee_info.wage_per_hr * work_hour
                print(f"Employee day{count_days}'s Wage is : {daily_wage}")
                monthly_wage = monthly_wage + daily_wage
                day = day + 1
            print(f"Company name is {employee_info.company_name}\nEmployee hours : {emp_hours} and Days : {day}")
            if emp_hours > 100:
                monthly_wage -= daily_wage
                emp_hours -= work_hour
                print(f"Employee hours : {emp_hours} and Days : {day}")
            self.company_dict[employee_info.company_name] = monthly_wage
            with open("D:\PythonBridgelabz\EmployeeWagePy\emp_wage.json",'a') as json_file:
                json.dump(self.company_dict, json_file)
            print(f"\nEmployee's Salary for the Entire Month is: {monthly_wage}\n")
        except Exception as e:
            print("Invalid", e)

    def find_wage_by_company(self, company):
        """
        -this method will check the company list and return the total wage.
        :param company:
        :return:Total_wage
        """
        try:
            if company in self.company_dict.keys():
                total_wage = self.company_dict.get(company)
                print(f"Total wage of {company} is Rs {total_wage}/-")
            else:
                print(f"{company} isn't present....\nTry another one...")
        except Exception as e:
            print("Invalid", e)
