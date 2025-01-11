# Override the __len__() method on vector of problem 5 to display the dimension of the 
# vector.

class Vector:
    
    def __init__(self, list):
        """
        Constructor to initialize the vector with a list of components.
        Stores the list as an attribute and assigns individual components to x, y, z.
        Example: Vector([1, 2, 3]) initializes a 3D vector with x=1, y=2, z=3.
        """
        self.list = list  # Store the entire list for later use
        self.x, self.y, self.z = list  # Assign the list values to x, y, z components
    
    def __str__(self):
        """
        String representation of the vector in the format 'xi + yj + zk'.
        Example: Vector([1, 2, 3]) -> "1i + 2j + 3k"
        """
        return f"{self.x}i + {self.y}j + {self.z}k"
            
    def __len__(self):
        """
        Return the number of components in the vector (i.e., its dimensions).
        Example: len(Vector([1, 2, 3])) -> 3
        """
        return len(self.list)

# Create one vector object
a = Vector([1, 2, 3])  # Initialize a vector with components [1, 2, 3]

# Print the vector representation
print(a)  # Output: "1i + 2j + 3k"

# Print the length of the vector (number of components)
print(len(a))  # Output: 3
