class Employee:
    def __init__(self,first,last) -> None:
        self.first = first
        self.last = last
        self.email = first+'.'+last+'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp1=Employee('mahmud','hossain')
emp2=Employee('toufikur','rahman')

print(emp1.email)
print(emp2.email)
print(emp1.fullname())
print(emp2.fullname())
#we need to explicitly define on which object we want to apply this method
print(Employee.fullname(emp2))
