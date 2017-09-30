###
# Author: ET
# This class is implemented to test the Rover Class. 
# Since Rover is a base class for the Rover object, in this test class we need to test the getters and setters
# and make sure that the object has always the correct values for the coordinates and direction. 
###

import unittest
import PlanetMars as pm

class TestPlanetMars(unittest.TestCase):
    planet = pm.PlanetMars()
    def test_extractCoord(self):
        """ Test function of reading the planet dimensions from input file"""
        self.assertEqual(self.planet.extract_coord("5 5"), [5, 5])
        self.assertRaises(ValueError, self.planet.extract_coord, "x y")
        self.assertRaises(ValueError, self.planet.extract_coord, "5.0 5.0")
    def test_extractRover(self):
        """ Test function of reading the coordinates and direction of a rover"""
        self.assertEqual(self.planet.extract_rover("1 2 N"), (1, 2, "N"))
        self.assertRaises(ValueError, self.planet.extract_rover, "N 2 N")
        self.assertRaises(ValueError, self.planet.extract_rover, "1 N N")
        self.assertRaises(ValueError, self.planet.extract_rover, "1,0 2 N")
        self.assertRaises(Exception, self.planet.extract_rover, "1 2")
        
    def test_extractMovements(self):
        """ Test function of reading the rovers movement from input file """
        self.assertEqual(self.planet.extract_movements("LMR"), ["L","M","R"])
 
                
if __name__ == '__main__':
    unittest.main()