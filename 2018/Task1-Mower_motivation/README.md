# Task 1: Mower motivation

Meet the Mowmaster 5000, the very latest in robotic gardening technology from a world-leading home-automation/weaponry company. The Mowmaster lets you put your feet up while it trims the grass, bins the cuttings – it can even walk the dog! Any resemblance to a small tank is purely coincidental and occasional news reports of mass carnage left in the wake of a summer’s lawnmowing have just made it cheaper to buy.

As well as a completely autonomous mode in which the Mowmaster blunders around a garden trimming grass and scaring small animals, the robot can download stored programs consisting of a series of commands, like this.

#MOWMASTER 5000 ALL YOUR LAWN BELONG TO US  
#Mow a square using the MOWMASTER 5000  
F5  
C  
F5  
C  
F5  
C  
F5  
C  
#Now some freestyling  
A  
F1  
C  
F22  
A  
F1  
C  
F68  
A  
F2  
F3  
C  
C  
F55   

The Mowmaster obeys a small number of instructions:

    C turns the Mowmaster 90 degrees clockwise from its current heading.
    A turns 90 degrees anticlockwise
    F(metres) e.g. F5 has the Mowmaster move forward 5 metres. The Mowmaster only moves a whole number of metres.

In a Mowmaster program, each instruction appears on its own line.

Any line beginning with the # character (we’re not going to get into an argument about what that’s called right now) is a programmer comment and is ignored by the robot.

#THE MOWMASTER 5000 IS AMAZING  

Is a comment and is not run, whilst:

F100000  
#GO FORWARD A LONG WAY  

Is an instruction to the robot (which will be executed), followed by a comment.

All instructions and comments begin in the first character of a line: there are no whitespace characters before an instruction or comment starts.

You can assume that all the lines are either comments or valid instructions: there's no need to validate the input file. In particular, there are no blank lines in the file.

In the example above, there are 3 comments and 22 instructions.

Part 1

Given the instructions file in 01-mowmaster.txt, how many instructions are there?


Meet the Mowmaster 5000, the very latest in robotic gardening technology from a world-leading home-automation/weaponry company. The Mowmaster lets you put your feet up while it trims the grass, bins the cuttings – it can even walk the dog! Any resemblance to a small tank is purely coincidental and occasional news reports of mass carnage left in the wake of a summer’s lawnmowing have just made it cheaper to buy.

As well as a completely autonomous mode in which the Mowmaster blunders around a garden trimming grass and scaring small animals, the robot can download stored programs consisting of a series of commands, like this.

#MOWMASTER 5000 ALL YOUR LAWN BELONG TO US  
#Mow a square using the MOWMASTER 5000  
F5  
C  
F5  
C  
F5  
C  
F5  
C  
#Now some freestyling  
A  
F1  
C  
F22  
A  
F1  
C  
F68  
A  
F2  
F3  
C  
C  
F55   

The Mowmaster obeys a small number of instructions:

    C turns the Mowmaster 90 degrees clockwise from its current heading.
    A turns 90 degrees anticlockwise
    F(metres) e.g. F5 has the Mowmaster move forward 5 metres. The Mowmaster only moves a whole number of metres.

In a Mowmaster program, each instruction appears on its own line.

Any line beginning with the # character (we’re not going to get into an argument about what that’s called right now) is a programmer comment and is ignored by the robot.

#THE MOWMASTER 5000 IS AMAZING  

Is a comment and is not run, whilst:

F100000  
#GO FORWARD A LONG WAY  

Is an instruction to the robot (which will be executed), followed by a comment.

All instructions and comments begin in the first character of a line: there are no whitespace characters before an instruction or comment starts.

You can assume that all the lines are either comments or valid instructions: there's no need to validate the input file. In particular, there are no blank lines in the file.

If the Mowmaster starts at x = 0, y = 0 and facing to the right, if it follows the instructions above it will end up at position x = 90, y = -48. As the Mowmaster can only travel in the cardinal directions, it would need to travel 90 + 48 = 138 metres to return to its starting place.

Part 2

The instructions are still file in 01-mowmaster.txt. After following those instructions, how far would the Mowmaster travel to return to its starting point? (Just enter the number of metres, not any units or similar.)
