import math

class Point:
    def _init_(self, x, y):
        self.x = x
        self.y = y

class Line:
    def _init_(self, start, end):
        self.start = start
        self.end = end
        self.length = self.compute_length()
        self.slope = self.compute_slope()

    def compute_length(self):
        return math.sqrt((self.end.x - self.start.x)*2 + (self.end.y - self.start.y)*2)

    def compute_slope(self):
        if (self.end.x - self.start.x) == 0:
            return float('inf')  # pendiente infinita (línea vertical)
        radians = math.atan2((self.end.y - self.start.y), (self.end.x - self.start.x))
        degrees = math.degrees(radians)
        return degrees

    def compute_horizontal_cross(self):
        # Devuelve True si cruza el eje X
        return (self.start.y * self.end.y) < 0

    def compute_vertical_cross(self):
        # Devuelve True si cruza el eje Y
        return (self.start.x * self.end.x) < 0

    def discretize_line(self, n):
        # Crea n puntos igualmente espaciados sobre la línea
        self.points_on_line = []
        for i in range(n):
            t = i / (n - 1)
            x = self.start.x + t * (self.end.x - self.start.x)
            y = self.start.y + t * (self.end.y - self.start.y)
            self.points_on_line.append(Point(x, y))
        return self.points_on_line
