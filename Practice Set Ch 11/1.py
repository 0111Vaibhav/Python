# Create a class (2-D vector) and use it to create another class representing a 3-D 
# vector

class TwoDimension:
    length = 15
    breadth = 30
    def __init__(self,dimension):
        print(f"Object of {dimension} created With : \nL = {self.length}\nB = {self.breadth}")

class ThreeDimension(TwoDimension):
    Height = 40
    def __init__(self,dimension):
        super().__init__(dimension)
        print(f"H = {self.Height}")
        
a = TwoDimension("2d")
b = ThreeDimension("3d")
