###
# Author ET
# Main Program. It will read the input file with the rovers initial positions and movements and it will print the final positions of each rover.
# All directions of the rovers can be considered as angles in the two dimensional coordinate system. Movements of the rovers are presented on how much should the 
# rover rotate in case of that movement. For instance if the current movement is Left the rover should rotate by 90degrees in the counterclock wise direction.
###

import sys
import Rover

class PlanetMars():
    allowed_movements = ['M', 'L', 'R']
    allowed_directions = ['E','N','W','S']
    movements = {'M':0, 'L':90, 'R':270}
    directions = {'E':0, 'N':90, 'W':180, 'S':270}
    
    def __init__(self):
        self.rovers = []
        self.instructions = []
        
    def readInput(self):
        """ Read the input file"""
        inFile = sys.argv[1]
        if isinstance(inFile, str):
            with open(inFile) as infile:
                lines = infile.read().splitlines()
                planet_coordinates = self.extract_coord(lines[0])
                for line in lines[1::2]:
                    (x,y,direction) = self.extract_rover(line)
                    newRover = Rover.Rover(x, y, direction)
                    self.rovers.append(newRover) 
                for line in lines[2::2]:
                    self.instructions.append(self.extract_movements(line))
                
        else:
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
                if direction in self.directions.keys():
                    return (x, y, direction)
                else:
                    raise ValueError("Incorrectly specified movement of the rover")
            except:
                raise ValueError("Coordinates of the rover must of of type integer")
        else:
            raise ValueError("Each rover must be specified by a tuple of three elements")
            
    def extract_movements(self, line):
        """ Read the movements that a Rover should perform in the planet"""
        return [i for i in line]
        
def main():
    mars = PlanetMars()
    mars.readInput()
    
if __name__ == '__main__':
    main()
        