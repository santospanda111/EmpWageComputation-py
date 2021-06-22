from EmpWageBuilder import EmpWageBuilder
import logging
logging.basicConfig(filename="emp_wage1.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    try:
        print('Welcome to Employee Wage Computation Program')
        companies = EmpWageBuilder()
        companies.add_company("Bridgelabz", 100, 20, 20)
        companies.add_company("Amazon", 100, 20, 15)
        for company in EmpWageBuilder.company_list:
            companies.calculate_monthly_wage(company)

        company = input("Enter the Company name to find monthly wage:\n")
        companies.find_wage_by_company(company)
    except Exception as e:
        print("Invalid", e)

    """Here i have implemented logging."""
    logger.debug("Debug Message....")
    logger.info("Information.....")
    logger.warning("Warning.....")
    logger.error("Error.....")
    logger.critical("Critical message....")
