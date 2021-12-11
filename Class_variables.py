class Employee:
    raise_amount = 1.04  #class variable
    employee_number = 0  #class variable

    def __init__(self,first,last,pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'

        Employee.employee_number += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)

print(Employee.employee_number)
emp1=Employee('mahmud','hossain',20000)
emp2=Employee('toufikur','rahman',18000)
#Employee.raise_amount = 1.05
emp1.raise_amount = 1.05
#print(emp1.__dict__)->To see emp1 obj attibutes
#print(Employee.__dict__)->To see Employee class attibutes
print(Employee.employee_number)
print(emp1.raise_amount)
print(emp1.__dict__)
print(emp2.raise_amount)
