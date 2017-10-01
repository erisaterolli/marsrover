###
# Author ET
# Main Program. It will read the input file with the rovers initial positions and movements and it will print the final positions of each rover.
###

import sys
import Rover
import RoverManager as rm
class PlanetMars():
    allowed_movements = ['M', 'L', 'R']
    allowed_directions = ['E','N','W','S']

    
    def __init__(self):
        self.rovers = []
        self.instructions = []
        self.coordinates = None
        
    def readInput(self):
        """ Read the input file"""
        try:
            inFile = sys.argv[1]
            if isinstance(inFile, str):
                with open(inFile) as infile:
                    lines = infile.read().splitlines()
                    self.coordinates = self.extract_coord(lines[0])
                    for line in lines[1::2]:
                        (x,y,direction) = self.extract_rover(line)
                        self.rovers.append([x, y, direction]) 
                    for line in lines[2::2]:
                        self.instructions.append(self.extract_movements(line))
                    
            else:
                raise ValueError("You must specify the name of the input file")
        except:
            raise ValueError("You must specify the name of the input file")
            
    
    def extract_coord(self,line):
        """ Retrun the coordinates of the planet (board) """
        try:
            dimensions = [int(i) for i in line.split(" ")]
            return dimensions
        except:
            raise ValueError("Both dimensitions of the planet must be of type integer")
            
    def extract_rover(self, line):
        """ Read the current position of a rover object"""
        rover_details = line.split(" ")
        if len(rover_details) == 3:
            direction = rover_details[2]
            try:
                x, y = int(rover_details[0]), int(rover_details[1])
                if direction in self.allowed_directions:
                    return (x, y, direction)
                else:
                    raise ValueError("Incorrectly specified direction of the rover")
            except:
                raise ValueError("Coordinates of the rover must of of type integer")
        else:
            raise ValueError("Each rover must be specified by a tuple of three elements")
            
    def extract_movements(self, line):
        """ Read the movements that a Rover should perform in the planet"""
        moves = []
        for i in line:
            if i in self.allowed_movements:
                moves.append(i)
            else:
                raise ValueError("Incorrectly specified direction of the rover")
        return moves
        
def main():
    mars = PlanetMars()
    mars.readInput()
    
    rvmanager = rm.RoverManager(mars.coordinates,mars.rovers, mars.instructions)
    rvmanager.createRoversObjects()
    rvmanager.launchRoversSequantially()
    
if __name__ == '__main__':
    main()
        