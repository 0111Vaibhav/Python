# Create a class “Programmer” for storing information of few programmers 
# working at Microsoft.

class Programmer:
    def __init__(self,name,salary,language):
        self.name = name
        self.salary =  salary
        self.language =  language
        print(f'''Object for new employee is created : 
Name = {name}
Salary = {salary}
Language = {language}''')

Employee = Programmer("Vaibhav",1000000,"Python")
        