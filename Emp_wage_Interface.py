from abc import *


class Emp_interface(ABC):
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
    def company_emp_wage(self):
        pass
