
class Rectangle:
    def __init__(self, lower_left, upper_right):
        # Lagre hjørnene (slik at info() kan skrive dem ut)
        self.lower_left = lower_left
        self.upper_right = upper_right

        # Samme logikk som i forelesningen
        self.width = upper_right[0] - lower_left[0]
        self.height = upper_right[1] - lower_left[1]
        
    def area(self):
        return self.width * self.height

    def info(self):
        """Skriv ut koordinatene til nedre venstre og øvre høyre hjørne."""
        print(f"Rectangle: lower_left={self.lower_left}, upper_right={self.upper_right}")


if __name__ == "__main__":
    # Lag en liste med tre ulike rektangler
    rectangles = [
        Rectangle((0.0, 0.0), (2.0, 1.0)),
        Rectangle((1.5, -0.5), (3.0, 2.5)),
        Rectangle((-2.0, -1.0), (0.5, 0.5)),
    ]

    # Kall info() for hvert rektangel
    for r in rectangles:
        r.info()