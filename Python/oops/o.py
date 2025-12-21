
# Encapsulation

# class Car:
#     model = ""
#     color = ""
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
    
#     def show(self):
#         print(f"Model: {self.model}")
#         print(f"Color: {self.color}")
    
#     def update(self, model, color):
#         self.model = model
#         self.color = color
    
# car1 = Car("Toyota", "Red")
# car2 = Car("Honda", "Blue")

# car1.show()
# car2.show()

# car1.update("Honda", "Black")
# car1.show()


# Inheritance

class Car:
    model = ""
    color = ""
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def show(self):
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
    
    def update(self, model, color):
        self.model = model
        self.color = color

class ElectricCar(Car):
    battery = 0
    def __init__(self, model, color, battery):
        super().__init__(model, color)
        self.battery = battery
    
    def show(self):
        super().show()
        print(f"Battery: {self.battery}")
    
    def update(self, model, color, battery):
        super().update(model, color)
        self.battery = battery
    


Ecar1 = ElectricCar("Toyota", "Red", 100)
Ecar2 = ElectricCar("Honda", "Blue", 200)

Ecar1.show()
Ecar2.show()

Ecar1.update("Honda", "Black", 300)
Ecar1.show()
