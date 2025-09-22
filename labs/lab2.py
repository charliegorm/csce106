import math

def circleA(radius):
    area = math.pi * radius**2
    return area
    
def rectA(length, width):
    area = length * width
    return area
    
def triA(base, height):
    area = 0.5 * base * height
    return area

while True:
    shape = input("Enter the shape for which area you want to calculate('Circle', 'Rectangle' or 'Triangle') or 'exit' to finish: ").lower()

    if shape == "exit":
        print("Goodbye!")
        break
    elif shape == "circle": 
        radius = float(input("Enter the parameter needed to calculate the area of a Circle ('radius'): "))
        print("The area of your circle is: ", circleA(radius))
    elif shape == "rectangle": 
        print("For a rectangle, you'll need to input the two parameters, length and width.")
        length = float(input("Enter your rectangle's length: "))
        width = float(input("Enter your rectangle's width: "))
        print("The area of your rectangle is: ", rectA(length,width))
    elif shape == "triangle": 
        print("For a triangle, you'll need to input the two parameters, base and height.")
        base = float(input("Enter your triangle's base: "))
        height = float(input("Enter your triangle's height: "))
        print("The area of your triangle is: ", triA(base,height))
    else:
        print("The shape you entered does not match any of the choices provided (Circle, Rectangle, Triangle)")
