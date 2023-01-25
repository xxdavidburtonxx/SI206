class Rectangle():
    # Create the constructor "__init__" method
    # Arguments: width (an ingeter), height (an integer)
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # It sets an instance variable, "width" to the passed argument, width
    # It sets an instance variable, "height" to the passed argument, height

    # YOUR CODE HERE



    # Create the "__str__" method
    #
    # It returns a string, 
    #       "A rectangle with width ____ and height ____"

    # YOUR CODE HERE
    def __str__(self):
        return "A rectangle with width " + str(self.width) + " and height " + str(self.height)


    # Create the "verify_input" method
    #
    # It returns a boolean
    #       True if the width and height are positive numbers
    #       False otherwise

    # YOUR CODE HERE

    def verify_input(self):
        if (self.width >= 0) & (self.height >= 0):
            return True
        else:
            return False

    # # Create the "area" method
    # #
    # # It first verifies inputs and return "Invalid input" if they are invalid.
    # # Otherwise, it returns the area of the rectangle.

    # # YOUR CODE HERE
    def area(self):
        if self.verify_input() == False:
            return "Invaluid input"
        else:
            return int(self.width) * int(self.height)



    # # Create the "perimeter" method
    # #
    # # It first verifies inputs and return "Invalid input" if they are invalid.
    # # Otherwise, it returns the perimeter of the rectangle.

    # # YOUR CODE HERE

    def perimeter(self):
        if self.verify_input() == False:
            return "Invaluid input"
        else:
            return 2*(int(self.width) + int(self.height))

def main():
    r = Rectangle(10, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

    r = Rectangle(0, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

if __name__ == "__main__":
    main()