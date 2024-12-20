class Vehicle:
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

    def get_license_plate(self):
        return self.license_plate

    def get_vehicle_type(self):
        return self.vehicle_type


class ParkingLevel:
    def __init__(self, total_spaces):
        self.total_spaces = total_spaces
        self.remaining_spaces = total_spaces.copy()
        self.vehicle_list = []

    def get_total_spaces(self):
        return self.total_spaces

    def get_remaining_spaces(self):
        return self.remaining_spaces

    def find_vehicle(self, license_plate):
        for vehicle in self.vehicle_list:
            if vehicle.get_license_plate() == license_plate:
                return True
        return False

    def add_vehicle(self, vehicle):
        vehicle_type = vehicle.get_vehicle_type()
        if self.remaining_spaces[vehicle_type] > 0:
            self.vehicle_list.append(vehicle)
            self.remaining_spaces[vehicle_type] -= 1
            print(
                f"{vehicle_type} vehicle ({vehicle.get_license_plate()}) is parked on this level."
            )
            return True
        return False

    def remove_vehicle(self, license_plate):
        for vehicle in self.vehicle_list:
            if vehicle.get_license_plate() == license_plate:
                self.vehicle_list.remove(vehicle)
                self.remaining_spaces[vehicle.get_vehicle_type()] += 1
                print(f"Vehicle ({license_plate}) was removed from this level.")
                return True
        return False


class ParkingGarage:
    def __init__(self, levels):
        self.levels = levels

    def get_total_spaces(self):
        total = {"Normal": 0, "Compact": 0, "Oversize": 0}
        for level in self.levels:
            for vehicle_type, count in level.get_total_spaces().items():
                total[vehicle_type] += count
        return total

    def get_remaining_spaces(self):
        remaining = {"Normal": 0, "Compact": 0, "Oversize": 0}
        for level in self.levels:
            for vehicle_type, count in level.get_remaining_spaces().items():
                remaining[vehicle_type] += count
        return remaining

    def find_vehicle(self, license_plate):
        for i, level in enumerate(self.levels):
            if level.find_vehicle(license_plate):
                print(f"Vehicle ({license_plate}) is on level {i + 1}.")
                return
        print(f"No vehicle with license plate {license_plate} found.")

    def add_vehicle(self, vehicle):
        for i, level in enumerate(self.levels):
            if level.add_vehicle(vehicle):
                print(f"{vehicle.get_vehicle_type()} vehicle ({vehicle.get_license_plate()}) is parked on level {i + 1}.")
                return
        print(f"No available space for {vehicle.get_vehicle_type()} vehicle ({vehicle.get_license_plate()}).")

    def remove_vehicle(self, license_plate):
        for i, level in enumerate(self.levels):
            if level.remove_vehicle(license_plate):
                print(f"Vehicle ({license_plate}) was removed from level {i + 1}.")
                return
            print(f"No vehicle with license plate {license_plate} found.")

    def print_garage(self):
        print("Total Spaces")
        for vehicle_type, count in self.get_total_spaces().items():
            print(f"{vehicle_type} ({count})")
        print("\nRemaining Spaces")
        for i, level in enumerate(self.levels):
            print(f"Level {i + 1}: {level.get_remaining_spaces()}")


vehicle_1 = Vehicle("EDL6776", "Compact")
vehicle_2 = Vehicle("BLB9665", "Normal")
vehicle_3 = Vehicle("PHE9858", "Compact")
vehicle_4 = Vehicle("MEI3923", "Compact")
vehicle_5 = Vehicle("NDL2511", "Compact")

level_1 = ParkingLevel({"Normal": 4, "Compact": 2, "Oversize": 2})
level_2 = ParkingLevel({"Normal": 3, "Compact": 1, "Oversize": 1})
level_3 = ParkingLevel({"Normal": 3, "Compact": 2, "Oversize": 2})

garage = ParkingGarage([level_1, level_2, level_3])

garage.add_vehicle(vehicle_1)
garage.add_vehicle(vehicle_2)
garage.add_vehicle(vehicle_3)
garage.add_vehicle(vehicle_4)
garage.add_vehicle(vehicle_5)

garage.print_garage()

garage.find_vehicle("NDL2511")
garage.remove_vehicle("NDL2511")

garage.print_garage()
