from abc import *


class EmpInterface(ABC):
    """
    -Here i have added interface approach
    -In which i have added abstract methods and later i have implemented by Emp_wage_builder class.
    """

    @abstractmethod
    def check_attendance(self):
        pass

    @abstractmethod
    def calculate_monthly_wage(self, company):
        pass

    @abstractmethod
    def add_company(self, company_name, max_hr_per_month, total_days, wage_per_hr):
        pass

    @abstractmethod
    def find_wage_by_company(self, company):
        pass
