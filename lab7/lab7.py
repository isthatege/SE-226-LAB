class Vehicle:
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model = model
        self.year = int(year)

    def __str__(self):
        return f"VID: {self.vid} | {self.model} ({self.year})"

    def __eq__(self, other):
        if isinstance(other, Vehicle):
            return self.vid == other.vid
        return False

    def is_new(self, n):
        return (2026 - self.year) <= n


class Car(Vehicle):
    def __init__(self, vid, model, year, fuel_type, doors):
        super().__init__(vid, model, year)
        self.fuel_type = fuel_type
        self.doors = int(doors)

    def __str__(self):
        return f"[Car] {super().__str__()} | Fuel: {self.fuel_type} | {self.doors} Doors"


class Truck(Vehicle):
    def __init__(self, vid, model, year, max_load, axles):
        super().__init__(vid, model, year)
        self.max_load = int(max_load)
        self.axles = int(axles)

    def __str__(self):
        return f"[Truck] {super().__str__()} | Load: {self.max_load}kg | {self.axles} Axles"


class Motorcycle(Vehicle):
    def __init__(self, vid, model, year, engine_cc, v_type):
        super().__init__(vid, model, year)
        self.engine_cc = int(engine_cc)
        self.type = v_type

    def __str__(self):
        return f"[Motorcycle] {super().__str__()} | Eng: {self.engine_cc}cc | Type: {self.type}"


def save_fleet_to_file(vehicles, filename):
    with open(filename, 'w') as file:
        for v in vehicles:
            if isinstance(v, Car):
                file.write(f"Car,{v.vid},{v.model},{v.year},{v.fuel_type},{v.doors}\n")
            elif isinstance(v, Truck):
                file.write(f"Truck,{v.vid},{v.model},{v.year},{v.max_load},{v.axles}\n")
            elif isinstance(v, Motorcycle):
                file.write(f"Motorcycle,{v.vid},{v.model},{v.year},{v.engine_cc},{v.type}\n")


def load_fleet_from_file(filename):
    loaded_vehicles = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) < 2:
                    continue

                v_type = data[0]
                if v_type == 'Car':
                    loaded_vehicles.append(Car(data[1], data[2], data[3], data[4], data[5]))
                elif v_type == 'Truck':
                    loaded_vehicles.append(Truck(data[1], data[2], data[3], data[4], data[5]))
                elif v_type == 'Motorcycle':
                    loaded_vehicles.append(Motorcycle(data[1], data[2], data[3], data[4], data[5]))
        return loaded_vehicles
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []


if __name__ == "__main__":
    my_fleet = [
        Car("V001", "Tesla Model Y", 2023, "Electric", 4),
        Car("V002", "BMW 320i", 2018, "Petrol", 4),
        Truck("T101", "Volvo FH16", 2019, 25000, 6),
        Truck("T102", "Mercedes Actros", 2021, 18000, 4),
        Motorcycle("M301", "Yamaha R1", 2023, 998, "Sport"),
        Motorcycle("M302", "Harley Davidson", 2015, 1200, "Cruiser")
    ]

    save_fleet_to_file(my_fleet, "fleet.txt")

    print("Loading fleet data from 'fleet.txt'...")
    fleet_from_file = load_fleet_from_file("fleet.txt")
    print(f"{len(fleet_from_file)} vehicles loaded successfully.\n")

    print("--- All Vehicles ---")
    for vehicle in fleet_from_file:
        print(vehicle)
    print()

    print("--- Recent Vehicles (Last 4 Years) ---")
    for vehicle in fleet_from_file:
        if vehicle.is_new(4):
            print(vehicle)
    print()

    print("--- Electric Cars Only ---")
    for vehicle in fleet_from_file:
        if isinstance(vehicle, Car) and vehicle.fuel_type == "Electric":
            print(vehicle)