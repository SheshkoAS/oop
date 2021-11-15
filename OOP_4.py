class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
    def start_car(self):
        return "Автомобиль заведен"
    def stop_car(self):
        return "Автомобиль заглушен"
    def update_year_car(self, year):
        self.year = year
        return year
    def update_type_car(self, type):
        self.type = type
        return type
    def update_color_car(self, color):
        self.color = color
        return color

auto_1 = Car("red", "Volga", 1989)
print(auto_1.start_car(), auto_1.stop_car(), auto_1.update_color_car("blue"), auto_1.update_year_car(2005), auto_1.update_type_car("Toyota"), sep="\n")