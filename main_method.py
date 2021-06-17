from EmpWageBuilder import EmpWageBuilder

if __name__ == '__main__':
    print('Welcome to Employee Wage Computation Program')
    companies = EmpWageBuilder()
    companies.add_company("Bridgelabz", 100, 20, 20)
    companies.add_company("Amazon", 100, 20, 15)
    for company in EmpWageBuilder.company_list:
        companies.calculate_monthly_wage(company)
