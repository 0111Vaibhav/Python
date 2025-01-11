#  Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
# which changes the value of increment based on the salary.
class Employee:
    # Class attributes: Default salary and increment percentage
    salary = 50000  # Base salary of the employee
    increment = 20  # Percentage increment by default

    # Getter for `salaryAfterIncrement` using the @property decorator
    @property
    def salaryAfterIncrement(self):
        """
        Calculate the salary after applying the increment.
        Formula: salary + (increment * salary) / 100
        Example: If salary = 50000 and increment = 20,
                 salaryAfterIncrement = 50000 + (20 * 50000) / 100 = 60000
        """
        return self.salary + (self.increment * self.salary) / 100

    # Setter for `salaryAfterIncrement` using the @property.setter decorator
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        """
        Adjust the increment percentage based on the new salary.
        Formula: increment = ((new_salary / current_salary) - 1) * 100
        Example: If new_salary = 60000 and current_salary = 50000,
                 increment = ((60000 / 50000) - 1) * 100 = 20.0
        """
        self.increment = ((salary / self.salary) - 1) * 100

# Create an instance of the Employee class
a = Employee()

# Set a new salaryAfterIncrement and automatically update the increment percentage
a.salaryAfterIncrement = 60000  # New salary is 60000
# Print the updated increment percentage
print(a.increment)  # Output: 20.0

    
        
        
    