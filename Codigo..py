class Rectangle:
    def _init_(self, p1, p2, p3, p4):
        self.lines = [
            Line(p1, p2),
            Line(p2, p3),
            Line(p3, p4),
            Line(p4, p1)
        ]

    def perimeter(self):
        return sum(line.length for line in self.lines)

    def slopes(self):
        return [line.slope for line in self.lines]

    def crosses_x_axis(self):
        return any(line.compute_horizontal_cross() for line in self.lines)

    def crosses_y_axis(self):
        return any(line.compute_vertical_cross() for line in self.lines)
