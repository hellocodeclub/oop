class Car:
    def __init__(self, licensePlate):
        self.licensePlate = licensePlate

#-----------------------------------------------------

class ParkingSlot:
    def __init__(self, row, spotNumber, level, car):
        self.row = row
        self.spotNumber = spotNumber
        self.level = level
        self.car = car

    def isAvailable(self):
        return self.car==None

    def park(self, vehicle):
        self.car = vehicle

    def removeVehicle(self):
        self.car = None

#------------------------------------------------------

class Level:
    def __init__(self,rows,levelNumber):
        self.levelNumber = levelNumber
        self.rows = rows
        self.spotsPerRow = 2
        self.parkingSlots = []
        self.availableSpots = rows * self.spotsPerRow

    def findAvailableSlot(self):
        if(self.availableSpots<=0):
            return None
        else:
            if(len(self.parkingSlots)==0): # The level is empty, all spots are free
                return ParkingSlot(0,0,0, None)
            else:
                lastCarParked = self.parkingSlots[-1]

            if(lastCarParked.spotNumber<self.spotsPerRow): # Check if there is free space in the row
                return ParkingSlot(lastCarParked.row,lastCarParked.spotNumber,self.levelNumber,None)
            if(lastCarParked.row<self.rows):
                return ParkingSlot(lastCarParked.row+1,0,self.levelNumber,None)

    def park(self, vehicle):
        freeParkingSpot = self.findAvailableSlot()
        if(not(freeParkingSpot)):
            return False
        else:
            freeParkingSpot.park(vehicle)
            self.parkingSlots.append(freeParkingSpot)
            self.availableSpots-=1
            return True

#----------------------------------------------------------------

class ParkingLot:
    def __init__(self, levels):
        self.levels = levels

    def park(self, car):
        for level in self.levels:
            if(level.park(car)):
                return True
            else:
                continue

        return False





