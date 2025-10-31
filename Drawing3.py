"""
drawing.py — Oppgave 1–3

Kilde: Rectangle-ideen er basert på forelesning 8 (kursets notatbok),
og er her utvidet med info(), draw(), samt nye klassene Triangle og Circle.
Fargerstøtte (color) og strektykkelse (linewidth) er lagt til.

Navn: Jakob
"""

from math import cos, sin, pi
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


# ------------------------- Enkel matplotlib-"turtle" -------------------------
class MatplotlibTurtle:
    """Minimal turtle som tegner linjer i matplotlib og lar oss bruke plt.show()."""
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect("equal", adjustable="datalim")
        self.ax.grid(True, alpha=0.2)
        self._x = 0.0
        self._y = 0.0
        self._tegner = False
        self._xs, self._ys = [], []

    def penup(self):
        self._tegner = False
        self._xs, self._ys = [], []

    def pendown(self):
        self._tegner = True
        self._xs, self._ys = [self._x], [self._y]

    def goto(self, x, y):
        x, y = float(x), float(y)
        if self._tegner:
            self._xs.append(x)
            self._ys.append(y)
        self._x, self._y = x, y

    def stroke(self, color="black", linewidth=1.5):
        if self._xs and self._ys:
            self.ax.add_line(Line2D(self._xs, self._ys, color=color, linewidth=linewidth))
            self._xs, self._ys = [], []

    def show(self):
        self.ax.autoscale()
        plt.show()


# ------------------------------- R E C T A N G L E ---------------------------
class Rectangle:
    def __init__(self, lower_left, upper_right, *, color="black", linewidth=1.5):
        # lagre hjørner + forelesningens bredde/høyde
        self.lower_left = lower_left
        self.upper_right = upper_right
        self.width = upper_right[0] - lower_left[0]
        self.height = upper_right[1] - lower_left[1]
        # stil
        self.color = color
        self.linewidth = linewidth

    def area(self):
        return self.width * self.height

    def info(self):
        print(
            f"Rectangle: lower_left={self.lower_left}, upper_right={self.upper_right}, "
            f"color={self.color}, linewidth={self.linewidth}"
        )

    def draw(self, turtle):
        x1, y1 = self.lower_left
        x2, y2 = self.upper_right
        corners = [(x1, y1), (x2, y1), (x2, y2), (x1, y2), (x1, y1)]
        turtle.penup()
        turtle.goto(*corners[0])
        turtle.pendown()
        for p in corners[1:]:
            turtle.goto(*p)
        if hasattr(turtle, "stroke"):
            turtle.stroke(self.color, self.linewidth)


# -------------------------------- T R I A N G L E ---------------------------
class Triangle:
    def __init__(self, p1, p2, p3, *, color="tab:blue", linewidth=1.5):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.color = color
        self.linewidth = linewidth

    def info(self):
        print(
            f"Triangle: p1={self.p1}, p2={self.p2}, p3={self.p3}, "
            f"color={self.color}, linewidth={self.linewidth}"
        )

    def area(self):
        # Shoelace-formelen for triangel
        x1, y1 = self.p1
        x2, y2 = self.p2
        x3, y3 = self.p3
        return abs(0.5 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)))

    def draw(self, turtle):
        seq = [self.p1, self.p2, self.p3, self.p1]
        turtle.penup()
        turtle.goto(*seq[0])
        turtle.pendown()
        for p in seq[1:]:
            turtle.goto(*p)
        if hasattr(turtle, "stroke"):
            turtle.stroke(self.color, self.linewidth)


# --------------------------------- C I R C L E ------------------------------
class Circle:
    def __init__(self, center, radius, *, color="tab:green", linewidth=1.5, segments=180):
        self.center = center
        self.radius = float(radius)
        self.color = color
        self.linewidth = linewidth
        self.segments = int(segments)

    def info(self):
        print(
            f"Circle: center={self.center}, radius={self.radius}, "
            f"color={self.color}, linewidth={self.linewidth}, segments={self.segments}"
        )

    def area(self):
        return pi * self.radius * self.radius

    def draw(self, turtle):
        cx, cy = self.center
        n = max(12, self.segments)
        points = []
        for i in range(n + 1):
            a = 2 * pi * i / n
            x = cx + self.radius * cos(a)
            y = cy + self.radius * sin(a)
            points.append((x, y))
        turtle.penup()
        turtle.goto(*points[0])
        turtle.pendown()
        for p in points[1:]:
            turtle.goto(*p)
        if hasattr(turtle, "stroke"):
            turtle.stroke(self.color, self.linewidth)


# ---------------------------------- D E M O ---------------------------------
if __name__ == "__main__":
    # Opprett én felles turtle
    t = MatplotlibTurtle()

    # Noen rektangler i ulike farger
    rects = [
        Rectangle((0, 0), (2, 1), color="black", linewidth=2.0),
        Rectangle((2.5, 0.5), (4.5, 2.5), color="tab:red", linewidth=1.5),
        Rectangle((-2, -1), (1, 1), color="tab:purple", linewidth=1.0),
    ]

    # Noen trekanter i ulike farger
    tris = [
        Triangle((0, 0), (1.5, 2.0), (3.0, 0.2), color="tab:blue", linewidth=2.0),
        Triangle((-3, -1), (-1, 2), (-2.5, 2.8), color="tab:orange", linewidth=1.5),
    ]

    # Sirkel + kvadrat som sirkel akkurat passer i (test av korrekt tegning)
    c = Circle(center=(6, 1.5), radius=1.2, color="tab:green", linewidth=2.0, segments=180)
    square = Rectangle((c.center[0]-c.radius, c.center[1]-c.radius),
                       (c.center[0]+c.radius, c.center[1]+c.radius),
                       color="tab:gray", linewidth=1.0)

    # Skriv info og tegn alt
    for r in rects:
        r.info()
        r.draw(t)

    for tri in tris:
        tri.info()
        tri.draw(t)

    c.info()
    c.draw(t)
    square.draw(t)

    # Vis figuren (kravet om plt.show())
    t.show()
