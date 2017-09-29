###
# Author: ET
# This class is implemented to test the Rover Class. 
# Since Rover is a base class for the Rover object, in this test class we need to test the getters and setters
# and make sure that the object has always the correct values for the coordinates and direction. 
###

import unittest
import Rover as rv

class TestRover(unittest.TestCase):
    
    coord_x = 3
    coord_y = 2
    direction = 90
    rover = rv.Rover(coord_x, coord_y,direction)
    
    def testInitialization(self):
        rover = rv.Rover(self.coord_x, self.coord_y, self.direction)
        self.assertEqual(rover.x, self.coord_x)
        self.assertEqual(rover.y, self.coord_y)
        self.assertEqual(rover.direction, self.direction)
    def test_getCoordinates(self):
        x,y = self.rover.getPosition()
        self.assertEqual(x, self.coord_x)
        self.assertEqual(y, self.coord_y)
    def test_direction(self):
        self.rover.direction = 20000
        self.assertGreater( self.rover.direction, 360)
        self.rover.direction = 900
        self.assertGreater( self.rover.direction, 360)
        self.rover.direction = -400
        self.assertGreater( self.rover.direction, 360)
    
                
if __name__ == '__main__':
    unittest.main()