# Task 3: Mower graffiti
Your Mowmaster 5000 has just received an update to its software that allows you to mow decorative patterns into your lawn by raising and lowering the grass cutting blades. To achieve this, two new commands have been added to the Mowmaster programming language:

    U raises the blades so that grass isn't cut.
    D lowers the blades to trim the grass close to the ground.

The Mowmaster still understands the C, A, and F commands, and still ignores comments in its program. See Task 1 for full information about the Mowmaster and its programs. For ease of reference, the commands are:

    C turns the Mowmaster 90 degrees clockwise from its current heading.
    A turns 90 degrees anticlockwise
    F(metres) e.g. F5 has the Mowmaster move forward 5 metres. The Mowmaster only moves a whole number of metres.
    # marks a program comment: this line is ignored.

This is a simple program using the new commands to make a simple pattern on the lawn.

#MOWMASTER 5000 ALL YOUR LAWN BELONG TO US  
#MOW A THREE BY THREE CHECKERED PATTERN  
D  
U  
F2  
D  
C  
#END OF THE FIRST COLUMN  
U  
F1  
C  
F1  
D  
U  
F1  
A  
#END OF THE SECOND COLUMN  
F1  
A  
D  
U  
F2  
D  

This program mows this pattern:  

⌷_⌷  
\_⌷\_   
⌷_⌷  

a total of five patches of grass. 

Assume the Mowmaster starts in the south-west corner of the lawn, facing north. The lawn extends much further north and east then the Mowmaster will travel, and it will never go further south or west than its starting point. 

If the Mowmaster mows the same patch of lawn several times, it still only counts as one mown patch. 

Part 1

Given the instructions file in 03-graffiti.txt, how many patches of grass are mown?


Part 2

After mowing your lawn, what message did the Mowmaster leave? Given the instructions are still in the 03-graffiti.txt file.
