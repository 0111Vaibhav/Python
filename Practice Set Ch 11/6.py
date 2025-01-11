# Write __str__() method to print the vector as follows: 
# 7i + 8j +10k

class Vector:
    # Constructor to initialize a vector in 3D space
    def __init__(self, x, y, z):
        """
        Initialize the vector with x, y, and z components.
        Example: Vector(1, 2, 3) creates a vector 1i + 2j + 3k.
        """
        self.x = x  # Component along the x-axis
        self.y = y  # Component along the y-axis
        self.z = z  # Component along the z-axis

    # Define the string representation of a vector
    def __str__(self):
        """
        Return a string representation of the vector.
        Example: Vector(1, 2, 3) -> "1i + 2j + 3k"
        """
        return f"{self.x}i + {self.y}j + {self.z}k"

# Create one vector objects
a = Vector(1, 2, 3) 

# Represents the vector 1i + 2j + 3k
print(a)
 