class MenuItem:
    def _init_(self, name, price):
        self.name = name
        self.price = price

    def calculate_price(self):
        return self.price


class Beverage(MenuItem):
    def _init_(self, name, price, size):
        super()._init_(name, price)
        self.size = size


class Appetizer(MenuItem):
    def _init_(self, name, price, is_vegetarian):
        super()._init_(name, price)
        self.is_vegetarian = is_vegetarian


class MainCourse(MenuItem):
    def _init_(self, name, price, spicy_level):
        super()._init_(name, price)
        self.spicy_level = spicy_level


class Dessert(MenuItem):
    def _init_(self, name, price, calories):
        super()._init_(name, price)
        self.calories = calories


class Order:
    def _init_(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.calculate_price() for item in self.items)

    def apply_discount(self):
        total = self.calculate_total()
        if len(self.items) >= 5:
            return total * 0.9  # 10% de descuento
        return total


# Crear elementos del menú (mínimo 10)
menu = [
    Beverage("Coca-Cola", 2.5, "mediana"),
    Beverage("Café", 2.0, "pequeño"),
    Appetizer("Pan de ajo", 3.0, True),
    Appetizer("Alitas", 5.0, False),
    MainCourse("Pizza", 8.5, "medio"),
    MainCourse("Pasta", 9.0, "bajo"),
    MainCourse("Hamburguesa", 7.5, "alto"),
    Dessert("Helado", 3.5, 250),
    Dessert("Tarta", 4.0, 300),
    Dessert("Fruta", 2.0, 100)
]

# Crear pedido
order = Order()
order.add_item(menu[0])
order.add_item(menu[4])
order.add_item(menu[6])
order.add_item(menu[7])
order.add_item(menu[2])

# Mostrar totales
print("Total sin descuento:", order.calculate_total())
print("Total con descuento:", order.apply_discount())
