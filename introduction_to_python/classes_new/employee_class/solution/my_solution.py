class Employee():
    def __init__(self, name, employee_id, salary, years_at_company):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.years_at_company = years_at_company
    
example1 = Employee("Phil McPythons", 1, 120000, 6)
print(example1.name, example1.salary, example1.years_at_company)