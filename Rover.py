###
# Author: ET
# This class is the Base class for Rover object. 
# The Rover is represented as an point with coordinates x and y in a two dimensional coordinate system
# and with a direction that present the angle that the point has in the system. 
# For example: E:0, N = 90, W = 180, S:270.
# The direction is presented as a integer to allow more complex movements
# that might be added as features to the system in the future.
###

class Rover():
    def __init__(self, x, y, direction):
        """Initialize a new Rover object."""
        self.x = x
        self.y = y
        self.direction = direction    
    def getPosition(self):
        """Return Rover object x coordinate."""
        return self.x, self.y
            
    def getDirection(self):
        """Return Rover object current direction."""
        return self.direction
        
    def setDirection(self, new_direction):
        if isinstance(new_direction, int) and new_direction >= 0:
            self.direction = new_direction % 360
        else:
            raise ValueError("Direction of the Rover object must be a floating point number and a positive integer")
    
    