import datetime
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
    @classmethod
    def set_raise(cls,amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp1_str.split('-')
        return cls(first,last,pay)
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True


emp1=Employee('mahmud','hossain',20000)
emp2=Employee('toufikur','rahman',18000)
Employee.set_raise(1.56)
print(Employee.raise_amount)
print(emp1.raise_amount)
emp2.set_raise (1.34)
print(emp2.raise_amount)

emp1_str ='mahmud-hossain-30000'
new_emp1 = Employee.from_string(emp1_str)
print(new_emp1.email)
print(new_emp1.pay)
my_date = datetime.date(2021,12,11)
print(Employee.is_workday(my_date))
