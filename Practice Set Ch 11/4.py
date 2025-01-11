#  Write a class ‘Complex’ to represent complex numbers, along with overloaded 
# operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    # Constructor to initialize the real and imaginary parts of the complex number
    def __init__(self, r, i):
        self.r = r  # Real part
        self.i = i  # Imaginary part

    # Overloading the "+" operator to add two complex numbers
    def __add__(self, c2):
        # Adds the real parts and imaginary parts separately
        return Complex(self.r + c2.r, self.i + c2.i)

    # Overloading the "*" operator to multiply two complex numbers
    def __mul__(self, c2):
        # Computes the real part using the formula: (a*c - b*d)
        real_part = self.r * c2.r - self.i * c2.i
        # Computes the imaginary part using the formula: (a*d + b*c)
        imag_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part, imag_part)

    # Method to define the string representation of a Complex object
    def __str__(self):
        # Displays the complex number in the form "a + bi"
        return f"{self.r} + {self.i}i"

# Creating two complex number objects
a = Complex(2, 5)  # Represents 2 + 5i
b = Complex(6, 2)  # Represents 6 + 2i

# Adding the two complex numbers using the "+" operator
print(a + b)  # Output: 8 + 7i

# Multiplying the two complex numbers using the "*" operator
print(a * b)  # Output: 2*6 - 5*2 (real part) + (2*2 + 5*6)i = 2 + 34i
