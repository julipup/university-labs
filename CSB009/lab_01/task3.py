# Згідно з варіантом розробити клас та консольний додаток для демонстрації
# функціоналу класу. Клас має містити два атрибути-даних (див.
# в табл. 1 стовпець «Атрибути 1 та 2») і чотири атрибути-методи:

# - метод для ініціалізації інстансу (метод має містити аргументи за замовчуванням);
# - метод формування рядка з інформацією про інстанс;
# - методи обробки атрибутів-даних за варіантом (див. в табл. 1 стовпці «Метод_1 обробки атрибутів»
# та «Метод_2 обробки атрибутів»).

# Варіант №7

class CarRide:
    def __init__(self, speed: float, travel_time: float):
        self.speed = speed # m/s
        self.travel_time = travel_time # minutes

    # returns distance in meters
    def get_distance(self) -> float:
        return self.speed * (self.travel_time * 60)

    def get_alternative_speed(self, time_multiplier: float = 0.5):
        # Calculating alternative speed
        # that is needed to cross { self.get_distance }
        # in { self.travel_time * time_multiplier }
        distance = self.get_distance()
        needed_time = self.travel_time * time_multiplier

        return (distance / needed_time) / 60

    def __str__(self):
        return f'CarRide <speed: { self.speed }, travel_time: { self.travel_time }, get_distance: { self.get_distance() } m.>'


# Console application
if __name__ == "__main__":
    # Creating new CarRide instance
    car_speed = float(input("| Car speed (m/s) = "))
    car_time = float(input("| Car travel time (min.) = "))

    ride = CarRide(car_speed, car_time)

    print("CarRide Instance:", ride)
    print(f'Speed, needed to ride { ride.get_distance() } m. in { ride.travel_time / 2 } min.:', ride.get_alternative_speed(0.5))
