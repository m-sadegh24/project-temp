class Vehicle:
    def __init__(self, name, max_speed, mileage, capacity=50):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self):
        return f'capacity = {self.capacity}'

    def fare (self):
        return self.capacity * 100

class Bus(Vehicle):

    def fare(self):
        return  super().fare() * 1.1

v = Vehicle('nissan', 130, 999999)
print(v.max_speed,v.mileage)
print(v.fare())
b = Bus('Tesla', 180, 9999999, 60)
print(b.fare())

print("kale pacheeee")