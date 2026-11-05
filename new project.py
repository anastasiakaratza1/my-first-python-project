
class Employee:

    """
    The parent class for the Employees in company XXX
    
    """
    def __init__(self, name: str, salary: float):
        self.name=name
        self.salary=salary
    
    def get_details(self):
        print (f"Employee with name {self.name} earns {self.salary: .1f} euros")


class Manager (Employee):
    def promote(self,employee: Employee):
        employee.salary = employee.salary *1.1
        print(employee.get_details())
    
class Developer (Employee):
    def __init__(self,name: str,salary: float, programming_language: str):
        super().__init__(name,salary)
        self.programming_language = programming_language

manager1= Manager (name= "Maria",salary= 2000)
developer1 = Developer ( name="Katerina",salary=3000, programming_language="python")
manager1.get_details()
developer1.get_details()
print ("============================")

manager1.promote(developer1) 
manager1.get_details()
developer1.get_details()





      
