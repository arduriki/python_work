class Employee:
    """Creates an employee for the company."""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, salary_raise=5_000):
        self.annual_salary += salary_raise