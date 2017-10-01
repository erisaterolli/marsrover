###
# Author: ET
# This class is the Base class for RoverManager that would serve as base class to launch the rovers and manage their movements in the planet
# All directions of the rovers can be considered as angles in the two dimensional coordinate system. Movements of the rovers are presented on how much should the 
# rover rotate in case of that movement. For instance if the current movement is Left the rover should rotate by 90degrees in the counterclock wise direction.
###
import Rover

class RoverManager():
    movements = {'M':0, 'L':90, 'R':270}
    directions = {'E':0, 'N':90, 'W':180, 'S':270}
    opp_directions = {0:'E', 90:'N', 180:'W', 270:'S'}
    
    def __init__(self, coordinates, rovers_initial, instructions):
        """Initialize a new Rover object."""
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.rovers_initial = rovers_initial
        self.rovers = []
        self.instrucions = instructions
        self.occupied_position = [[False]*(self.x+1)]*(self.y+1)
        
    def createRoversObjects(self):
        """Launches rovers in the planet"""
        for ind in range(len(self.rovers_initial)):
            currentRover = self.rovers_initial[ind]
            self.addRover(currentRover)
    
    def addRover(self, currentRover):
        """Add a new rover object"""
        [x,y,direction] = currentRover
        if self.insidePlanet(x,y) and not self.occupied_position[x][y]:
            self.rovers.append(Rover.Rover(x, y, self.directions[direction]))
        else:
            raise Exception("Outside boarders or occupied place")
            
    def insidePlanet(self, x, y):
        """Checks if position with coordinates x and y in avaible and inside the planet"""
        return (0 <= x <= self.x and 0 <= y <= self.y)
             
     
    def launchRoversSequantially(self):
        for ind in range(len(self.rovers)):
            current_rover = self.rovers[ind]
            current_movements = self.instrucions[ind]
            for mov in current_movements:
                if mov == 'L':
                    self.turnLeft(current_rover)  
                elif mov == 'R':
                    self.turnRight(current_rover) 
                elif mov == 'M':
                    self.moveForward(current_rover)
            final_x, final_y = current_rover.getPosition()
            self.occupied_position[final_x][final_y] = True
            print final_x, final_y, self.opp_directions[current_rover.getDirection()]
    def turnLeft(self, rover):
        """Turns the rover 90 degree to the left"""
        rover.setDirection(rover.getDirection() + self.movements['L'])
    
    def turnRight(self, rover):
        """Turns the rover 90 degree to the right"""
        rover.setDirection(rover.getDirection() + self.movements['R'])
        
    def moveForward(self,rover):
        """ Move one cell forward in the same direction of the rover"""
        current_x, current_y = rover.getPosition()
        current_direction =  rover.getDirection()
        new_x = None
        new_y = None
        if current_direction == 0:
            new_x = current_x + 1
            new_y = current_y
        elif current_direction == 90:
            new_x = current_x
            new_y = current_y + 1
        elif current_direction == 180:
            new_x = current_x - 1
            new_y = current_y
        elif current_direction == 270:
            new_x = current_x
            new_y = current_y - 1
        else:
            new_x = current_x
            new_y = current_y   
        if self.insidePlanet(new_x, new_y) :
            rover.x = new_x
            rover.y = new_y
        else:
            raise Exception("Rover can only move to a free place inside the planet")
        
   
        
def main():
    mars = RoverManager([5,5], [[2,2 ,'E']], [['M', 'M', 'R', 'M', 'M', 'R', 'M', 'R', 'R', 'M']])
    mars.createRoversObjects()
    mars.launchRoversSequantially()
    
    
if __name__ == '__main__':
    main()
        
            
        
        
            
            
        
        
        
    
        
        
        
    
        
    
    