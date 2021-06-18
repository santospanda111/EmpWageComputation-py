class Emp_Wage_Exception(Exception):
    """
    Creating a class for custom exceptions which is inherited Exception class
    """

    def __init__(self, message):
        super().__init__(message)
