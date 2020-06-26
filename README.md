#Introduction:

This repository is an implementation of a simple robot with limited navigation:

The robot needs to is controlled remotely by sending commands. These commands are written into a file as follows: 

```  
R 
F 
L 
F 
```

Where `R` stands for turn right, `F` stands for move forward 1 space and `L` stands for turn left. These are the only commands available to the robot. The robot moves on a 2D grid so that a turn is exactly 90 degrees. The turn is completed in place and so only rotation occurs. 
This repository implements two main feature sets for such a robot:

1. Calculating the distance travelled by the robot from the starting point (0,0) to its finishing point. The input of the program is the filename of commands and the output the distance (3 decimal places). 
  
 In the example above the output would be 1.414 units. 
  
2. The library's operate() function returns True or False if the commands sent at any point complete a loop (the robot visits (0,0) again during the journey). For example, the above commands would return False.

 However, the below command 

 ```
F  
R 
F 
R 
F 
R 
F 
```
  
 Would return True.

#Implementations
This repositiory contains two implementations:
##prototype/
A low fidelity prototype aimed at verifying that algorithmic ideas work with some basic unit testing for the core concepts

##robot/
A high fidelity implementation. BDD features and steps reside in features/

##READMEs
Each of these implementations has its own README markdown file with instruction for testing, running and design discussions.

