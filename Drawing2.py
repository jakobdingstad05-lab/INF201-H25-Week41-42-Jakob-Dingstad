"""
drawing.py — Oppgave 2: Tegne rektangler med turtle-grafikk
"""

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


class MatplotlibTurtle:
    """En enkel 'turtle' som tegner linjer med matplotlib slik at plt.show() fungerer."""
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect("equal", adjustable="datalim")
        self.ax.grid(True, alpha=0.2)
        self._x = 0.0
        self._y = 0.0
        self._tegner = False
        self._xs, self._ys = [], []

    def penup(self):
        """Løfter pennen (slutter å tegne)."""
        self._tegner = False
        self._xs, self._ys = [], []

    def pendown(self):
        """Setter pennen ned (begynner å tegne)."""
        self._tegner = True
        self._xs, self._ys = [self._x], [self._y]

    def goto(self, x, y):
        """Flytter 'turtlen' til et nytt punkt."""
        x, y = float(x), float(y)
        if self._tegner:
            self._xs.append(x)
            self._ys.append(y)
        self._x, self._y = x, y

    def stroke(self, farge="black", tykkelse=1.5):
        """Tegner linja som er samlet opp så langt."""
        if self._xs and self._ys:
            self.ax.add_line(Line2D(self._xs, self._ys, color=farge, linewidth=tykkelse))
            self._xs, self._ys = [], []

    def show(self):
        """Viser tegningen."""
        self.ax.autoscale()
        plt.show()


class Rectangle:
    """Rektangel definert av nedre venstre og øvre høyre hjørne."""
    def __init__(self, nedre_venstre, ovre_høyre):
        self.nedre_venstre = nedre_venstre
        self.ovre_høyre = ovre_høyre
        self.bredde = ovre_høyre[0] - nedre_venstre[0]
        self.høyde = ovre_høyre[1] - nedre_venstre[1]

    def area(self):
        """Returnerer arealet av rektangelet."""
        return self.bredde * self.høyde

    def info(self):
        """Skriver ut koordinatene til hjørnene."""
        print(f"Rektangel: nedre_venstre={self.nedre_venstre}, ovre_høyre={self.ovre_høyre}")

    def draw(self, turtle):
        """Tegner rektangelet med den gitte turtle."""
        x1, y1 = self.nedre_venstre
        x2, y2 = self.ovre_høyre
        hjørner = [(x1, y1), (x2, y1), (x2, y2), (x1, y2), (x1, y1)]

        turtle.penup()
        turtle.goto(*hjørner[0])
        turtle.pendown()

        for punkt in hjørner[1:]:
            turtle.goto(*punkt)

        # Tegn linjen (kun nødvendig for denne enkle matplotlib-turtlen)
        if hasattr(turtle, "stroke"):
            turtle.stroke()


if __name__ == "__main__":
    # 1. Opprett én turtle
    t = MatplotlibTurtle()

    # 2. Lag tre rektangler
    rektangler = [
        Rectangle((0.0, 0.0), (2.0, 1.0)),
        Rectangle((1.5, -0.5), (3.0, 2.5)),
        Rectangle((-2.0, -1.0), (0.5, 0.5)),
    ]

    # 3. Kall info() og tegn hvert rektangel med samme turtle
    for r in rektangler:
        r.info()
        r.draw(t)

    # 4. Vis figuren
    t.show()
