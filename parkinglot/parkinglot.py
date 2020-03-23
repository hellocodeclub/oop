class Car:
    def __init__(self, licensePlate):
        self.licensePlate = licensePlate

    def licensePlate(self):
        return self.licensePlate

class ParkingLot:
    def __init__(self, levels):
        self.levels = levels

    def park(self, car):
        for level in self.levels:
            freeParkingSlot = level.findFreeParkingSlot()
            if(freeParkingSlot):
                level.park(car)
                return True
            else:
                continue

        return False

class Level:
    def __init__(self,rows,levelNumber):
        self.levelNumber = levelNumber
        self.rows = rows
        self.spotsPerRow = 2
        self.parkingSlots = []
        self.availableSpots = rows * self.spotsPerRow

    def park(self, vehicle):
        freeParkingSpot = self.findFreeParkingSlot()
        if(not(freeParkingSpot)):
            return False
        else:
            freeParkingSpot.park(vehicle)
            self.parkingSlots.append(freeParkingSpot)
            self.availableSpots-=1
            return True


    def findFreeParkingSlot(self):
        if(self.availableSpots<=0):
            return None
        else:
            lastCarParked = self.lastCarParked()
            if(not(lastCarParked)):
                return ParkingSlot(0,0,0, None)

            elif(lastCarParked.spotNumber<self.spotsPerRow):
                return ParkingSlot(lastCarParked.row,lastCarParked.spotNumber,self.levelNumber,None)
            elif(lastCarParked.row<self.rows):
                return ParkingSlot(lastCarParked.row+1,0,self.levelNumber,None)
            else:
                return None

    def lastCarParked(self):
        if(len(self.parkingSlots)==0):
            return None
        else:
            return self.parkingSlots[-1]

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

    def getRow(self):
        return self.row

    def getSpotNumber(self):
        return self.spotNumber

    def removeVehicle(self):
        self.car = None

