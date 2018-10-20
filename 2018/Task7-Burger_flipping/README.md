# Task 7: Burger flipping

You're preparing the burgers for the guests to eat. While your hand-crafted artisanal burgers taste excellent, they're all different sizes and cook at different speeds. As soon as each burger is cooked, you take it off the barbeque and add it to the pile, ready for serving. The trouble is, because the burgers are all different sizes and higgledy-piggledy in the pile, it looks really untidy, as well as being unstable. To avoid a burger avalanche disaster, you need to sort the burgers by size, so the largest burgers are at the bottom and the smallest are at the top. 

The way you rearrange the stack of burgers is to slide your spatula into the stack at some point and use it to flip over all the burgers above it. You can then flip over another part of the stack, and so on, until the stack is sorted. 

If you start with a stack that looks like this (the numbers are the burger widths in attoparsecs)

 9 
18 
22 
15 
13 

and flip the top three burgers, you end up with this position:

 9       22 
18       18 
22  -3->  9 
15       15 
13       13 

If you flip the top two, then all five, then the top two, then the top three, you end up sorting the stack. The process looks like this.

 9       22       13       15        9 
18       18       15       13       13 
22  -3->  9  -5->  9  -2->  9  -3-> 15 
15       15       18       18       18 
13       13       22       22       22 

After these four flips, the stack is sorted.

Sorting your own stack is fairly easy. But you've got a lot of guests to feed, all your friends are working flat-out on their own Inceraptor THX-1138s, and no-one has any time to sort the burgers they're cooking. 

The good news is that you have a consignment of ZX42b burger-flipping attachments you can add to your Mowmaster 5000, so it can sort the burgers while it's delivering them from the cooks to the guests. The bad news is that each ZX42b only executes a particular sequence of flips, so you need to tell the Mowmaster which ZX42b to use for each stack. 

For instance, the stack 9 18 22 15 13 will be sorted by the ZX42b with instructions 3 5 2 3, and by the ZX42b with instructions 3 5 3 2 3 2. However, the ZX42b with instructions 4 5 3 4 2 3 won't sort the stack (you end up with 9 22 13 18 15, which is wrong).

Your ZX42b sorters are described in 07-flips.txt. The first line of the file starts burgers: and gives the starting arrangement of burgers. The subsequent lines describe the sorters, one per line, giving the sequence of flips each executes. Each sorter line starts with the number of the sorter.

For example, the file would look like this:

burgers: 9 11 3 5 10 8
01: 2 6 2 5 4 3
02: 2 6 2 5 1 4 3
03: 2 5 2 4
04: 2 6 2 5 1 4 1 3 2 1 2 1
05: 2 5 3 4
06: 5 6 3 5 2 4 1 3
07: 2 6 2 5 2 4 1 2
08: 2 6 2 5 1 4 1 3
09: 2 6 5 3 4 5 3
10: 3 5 2

(Sorter numbers are exactly two digits. There are 50 burgers in the stack, with sizes up to 10,000. The top of the stack is the first number; the bottom of the stack is the last number. Both burger sizes and flips are separated by a single space on each line.)

In this example, sorters 1, 2, 4, 8, and 9 would all sort the stack of burgers. Sorters 3, 5, 6, and 7 would not. 

Part 1

Given the stack of burgers and the sorters in 07-flips.txt, how many sorters would sort the given pile of burgers?


While you're preparing the burgers for distribution, your good friend Mirusíya says to you "Túsmi chifádhan tlagegrésa" ("You arrange the burgers clumsily"). Once the burger is cooked, one side will look more appetising than the other, and they're initially with that side uppermost. You'll want burgers to be in the sorted stack the same way up. But your method of sorting leaves some burgers upside-down!

If you keep track of the orientation of burgers, you see that your original method of sorting bugers does this. The stars mark upside-down burgers.

 9       22*      13*      15        9*
18       18*      15*      13       13*
22  -3->  9* -5->  9  -2->  9  -3-> 15*
15       15       18       18       18 
13       13       22       22       22 

To end up with all the burgers the right side up, you need to perform six flips, like this:

 9       22*      13*       9*      15*      13*       9 
18       18*      15*      15        9        9*      13 
22  -3->  9* -5->  9  -3-> 13  -2-> 13  -3-> 15  -2-> 15 
15       15       18       18       18       18       18 
13       13       22       22       22       22       22 

If you had the same set of sorters as the example before:

burgers: 9 11 3 5 10 8
01: 2 6 2 5 4 3
02: 2 6 2 5 1 4 3
03: 2 5 2 4
04: 2 6 2 5 1 4 1 3 2 1 2 1
05: 2 5 3 4
06: 5 6 3 5 2 4 1 3
07: 2 6 2 5 2 4 1 2
08: 2 6 2 5 1 4 1 3
09: 2 6 5 3 4 5 3
10: 3 5 2

only sorter 9 would correctly sort the burgers, leaving them in the correct size order and with all the burgers in their original orientation. 

Part 2

Your burgers and sorters are the same, still described in 07-flips.txt. But in this case, only one sorter will correctly sort the stack of burgers. Which sorter will correctly sort the given pile of burgers? (Give the ID number of the sorter.)
