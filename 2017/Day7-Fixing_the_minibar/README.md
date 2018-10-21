# Day 7: Fixing the minibar

After a good day sightseeing, it's back to the hotel and time for some refreshment. Unfortunately, the minibar in your room refuses to open. It's been hacked, with some ransomware! You'll need to provide the correct unlock code so you can get a nice, cold drink.

You could pay a large chunk of bitcoin, or you could defeat the ransomware some other way. 

You quickly find the schematics of the minibar lock. It's a fairly simple machine. It has four registers, a, b, c, d, and a special purpose pc register for the program counter. Each register can hold a 64-bit value (far bigger than any number in the programs you'll be running). You can assume all registers hold zero when the program starts.

On each clock tick, the machine executes the instruction pointed to by the pc, then increments pc. The machine halts when the machine tries to read from a location beyond the end of the program.

The machine has only a few instructions. They're listed by handy mnemonics:  
Minbar instructions Instruction 	Description  
inc r 	increment contents of register r  
dec r 	decrement contents of register r  
set r i 	set contents of register r to literal value i  
cpy r s 	copy contents of register r into register s  
jmp i 	jump to instruction i places forward  
jpz r i 	jump to instruction i places forward if register r contains zero, otherwise continue to next instruction  

Thejmp and jpz instructions jump relative to the current instruction, overriding the normal change in pc. jmp -1 would jump back to the previous instruction; jpz a 2 would skip the next instruction if register a contains zero.

Before you start execution of a program, you can set the values of some registers.

For example, this program multiplies the values in the a and b registers, leaving the result in the c register:

set c 0  
cpy a d  
jpz b 8  
dec b  
cpy d a  
jpz a 4  
inc c  
dec a  
jmp -3  
jmp -7  
set d 0  

Part 1

You think you've worked out how to generate the code wanted by the ransomware. The program is given in 07-program.txt, one instruction per line. 

Starting with register a holding 7, and all other registers holding zero, what does register a contain when the program finishes?


It seems your guess of 7 as the starting value was wrong.

Part 2

The program is still given in 07-program.txt, one instruction per line. 

Starting with register a holding 937, and all other registers and memory locations holding zero, what does register a contain when the program finishes?
