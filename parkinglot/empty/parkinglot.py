class Car:
    def __init__(self, licensePlate):
        self.licensePlate = licensePlate

    def licensePlate(self):
        return self.licensePlate
    
#-----------------------------------------------------------------------------

class ParkingSlot:
    def __init__(self, row, spotNumber, level, car):
        self.row = row
        self.spotNumber = spotNumber
        self.level = level
        self.car = car

    def isAvailable(self):
        # TODO
        # Return true is the spot is available(if empty), false otherwise
        # Note in case the spot is taken the class field self.car will contain a car
        return

    def park(self, vehicle):
        # TODO
        # Note if the self.car field has a car, it means there is a car parks in the parking slot
        return

    def removeVehicle(self):
        # TODO
        # Remove vehicle from parking slot
        # Note if the self.car field is empty, it means the parking slot is empty
        return

#-----------------------------------------------------------------------------

class Level:
    def __init__(self,rows,levelNumber):
        self.levelNumber = levelNumber
        self.rows = rows
        self.spotsPerRow = 2 # Two spots per row, feel free to change it :)
        self.parkingSlots = []
        self.availableSpots = rows * self.spotsPerRow

    def findAvailableSlot(self):
        # TODO
        # Return a free Parking Slot
        # Note a new car will be parked next to the last car
        # If there is no space in the row, then park it at the first place in the next row
        # If there is no spots available, return None
        return

    def park(self, vehicle):
        # TODO
        # This method will return true is the car was parked, and false otherwise
        return

#-----------------------------------------------------------------------------

class ParkingLot:
    def __init__(self, levels):
        self.levels = levels

    def park(self, car):
        # TODO
        # This method will return true is the car was parked, in false otherwise
        return

#-----------------------------------------------------------------------------



