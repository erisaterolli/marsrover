# Mars Rover Challenge

A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their on-board cameras can get a complete view of the surrounding terrain to send back to Earth.
 
A rover’s position and location is represented by a combination of x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.
 
In order to control a rover, NASA sends a simple string of letters. The possible letters are ‘L’, ‘R’ and ‘M’. ‘L’ and ‘R’ makes the rover spin 90 degrees left or right respectively, without moving from its current spot. ‘M’ means move forward one grid point, and maintain the same heading.
 
Assume that the square directly North from (x, y) is (x, y+1).

### Input
The problem below requires the input to be feeded by giving the name of textbased file.
### Output
The output for each rover will be printed in the standard output
#### Input and Output Examples
Test Input:

5 5

1 2 N

LMLMLMLMM

3 3 E

MMRMMRMRRM

Expected Output:

1 3 N

5 1 E

### Design and Assumption
The solution is based on OOP concepts. There are three main classes:

1. Rover: The base his class is the Base class for Rover object. The Rover is represented as an point with coordinates x and y in a two dimensional coordinate system
and with a direction that present the angle that the point has in the system. For example: E:0, N = 90, W = 180, S:270.
The direction is presented as a integer to allow more complex movements that might be added as features to the system in the future.

2. Rover Manager: This class is the Base class for RoverManager that would serve as base class to launch the rovers and manage their movements in the planet
All directions of the rovers can be considered as angles in the two dimensional coordinate system. Movements of the rovers are presented on how much should the 
rover rotate in case of that movement. For instance if the current movement is Left the rover should rotate by 90degrees in the counterclock wise direction.

3. PlanetMars: It is the Main Class that read and parse the input file, calls the appropriate modules for RoverManager Class and 
finally prints in the standard output the final positions of each rover in the planet.

In this version of the code a Rover can be directed in one of the horizontal directions 'NESW' and turn Left or Right and move one cell
forward. The Rover can not go outside the borders of the planet and can not move to a occupied cell by another rover.  

## Running the code
In order to run the code you have to open your terminal, navigate to the folder that contains the code and 
execute the following command, where inputFileName is the file that contains the Input Tests.

```
python PlanetMars.py inputFileName
```

### Running Test Cases for each Class

In order to run the unittest cases for each separate class you have to run the following command in your terminal

```
python ClassNameTest.py
```

## Authors

ET

