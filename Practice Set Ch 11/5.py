# Write a class vector representing a vector of n dimensions. Overload the + and * 
# operator which calculates the sum and the dot(.) product of them.

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

    # Overloading the "+" operator to add two vectors
    def __add__(self, other):
        """
        Add two vectors component-wise.
        Example: Vector(1, 2, 3) + Vector(4, 5, 6) -> Vector(5, 7, 9)
        """
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    # Overloading the "*" operator to compute the dot product
    def __mul__(self, other):
        """
        Calculate the dot product of two vectors.
        Formula: x1*x2 + y1*y2 + z1*z2
        Example: Vector(1, 2, 3) * Vector(4, 5, 6) -> 1*4 + 2*5 + 3*6 = 32
        """
        dot = self.x * other.x + self.y * other.y + self.z * other.z
        return dot  # Return the scalar result of the dot product

    # Define the string representation of a vector
    def __str__(self):
        """
        Return a string representation of the vector.
        Example: Vector(1, 2, 3) -> "1i + 2j + 3k"
        """
        return f"{self.x}i + {self.y}j + {self.z}k"

# Create two vector objects
a = Vector(1, 2, 3)  # Represents the vector 1i + 2j + 3k
b = Vector(4, 5, 6)  # Represents the vector 4i + 5j + 6k

# Add the two vectors using the overloaded "+" operator
print(a + b)  # Output: 5i + 7j + 9k

# Calculate the dot product of the two vectors using the overloaded "*" operator
print(a * b)  # Output: 32

    
    
        