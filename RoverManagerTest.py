import unittest
import RoverManager

class RoverManagerTest(unittest.TestCase):
    rm = RoverManager.RoverManager([5,5], [[2,2 ,'E']], [['M', 'M', 'R', 'M', 'M', 'R', 'M', 'R', 'R', 'M']])
    
    def test_addRover(self):
        """ Test  adding a new Rover in the Rover object List"""
        self.assertEqual(len(self.rm.rovers), 0)
        self.rm.addRover([2,2,'E'])
        self.assertEqual(len(self.rm.rovers), 1)
        
        # Adding a rover outside the boarder of the planet
        self.assertRaises(Exception, self.rm.addRover, [1, 6, 'S'])
        self.assertRaises(Exception, self.rm.addRover, [-1, 5, 'S'])
        self.assertRaises(Exception, self.rm.addRover, [-1, -1, 'S'])
        self.assertRaises(Exception, self.rm.addRover, [6, 6, 'S'])
         
    def test_insidePlanet(self):
        """ Test position of a rover is inside the planet """
        self.assertEqual(True, self.rm.insidePlanet(1,1))
        self.assertEqual(False, self.rm.insidePlanet(-1,1))     
           
    def test_turnLeft(self):
        """ Test moving to the left """
        self.rm.addRover([2,2,'E'])
        self.rm.turnLeft(self.rm.rovers[0])
        self.assertEqual(self.rm.rovers[0].getDirection(),90)
        
    def test_turnRight(self):
        """ Test moving to the right """
        self.rm.addRover([3,3,'E'])
        self.rm.turnRight(self.rm.rovers[1])
        self.assertEqual(self.rm.rovers[1].getDirection(),270)
        
    def test_moveForward(self):
        """ Test moving one cell forward """
        self.rm.moveForward(self.rm.rovers[0])
        x, y = self.rm.rovers[0].getPosition()
        self.assertEqual(x,3)
        self.assertEqual(y,2)
        
if __name__ == '__main__':
    unittest.main()