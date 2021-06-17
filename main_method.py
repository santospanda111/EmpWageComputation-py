from Company_emp_wage import Company_emp_wage
from Emp_wage_builder import Emp_wage_builder

if __name__ == '__main__':
    print('Welcome to Employee Wage Computation Program')
    bridgelabz = Company_emp_wage("Bridgelabz", 100, 20, 20)
    amazon = Company_emp_wage("Amazon", 100, 20, 15)
    """
    Here i have passed the objects of Company_employee_wage as parameters of Emp_wage_builder
    """
    companies = Emp_wage_builder(bridgelabz, amazon)
    companies.company_emp_wage()
