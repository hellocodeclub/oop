import unittest
from parkinglot.solution.parkinglot import ParkingLot, Level, Car

class MyTestCase(unittest.TestCase):
    def test_something(self):
        level1 = Level(rows=2,levelNumber=0)
        level2 = Level(rows=1,levelNumber=1)
        parkingLot = ParkingLot([level1,level2])

        # Fill first level
        self.assertEqual(True, parkingLot.park(Car('12345')))
        self.assertEqual(True, parkingLot.park(Car('12346')))
        self.assertEqual(True, parkingLot.park(Car('12347')))
        self.assertEqual(True, parkingLot.park(Car('12348')))

        #Fill second level
        self.assertEqual(True, parkingLot.park(Car('12350')))
        self.assertEqual(True, parkingLot.park(Car('12351')))


        self.assertEqual(False, parkingLot.park(Car('12349')))

    def test_level(self):
        level = Level(rows = 1,levelNumber=0)
        self.assertEqual(2, level.availableSpots)
        level.park(Car('l1'))
        level.park(Car('l2'))
        self.assertEqual(0, level.availableSpots)
def fillLevel(parkingLot):
    for spot in range(12):
        parkingLot.parkCar(Car('lic'+str(spot)))

if __name__ == '__main__':
    unittest.main()
