class InvalidRadiusError(Exception):
    def __init__(self, radius, message="Invalid radius"):
        self.radius = radius
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"Radius '{self.radius}' is invalid: {self.message}"

def calculate_area(radius):
    try:

        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        area = 3.14 * radius ** 2
        print(f"The area of the circle with radius {radius} is {area}.")
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

calculate_area(5)
calculate_area(-5)
