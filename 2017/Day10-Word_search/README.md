# Day 10: Word search
First nights in hotels are always a bit of an anticlimax, what with the recovery from travel and all. You decided to do one of your wordsearch puzzles.

These puzzles are a bit different from normal because they have a puzzle grid and a list of words, but only some of the words are in the puzzle; some of the words given are decoys and aren't present.

For instance, given the grid:

fhjpamownq  
wsdseuqeev  
ieaeladhcr  
piedtiriah  
rzsiwovspu  
oawhakieab  
browpcfrda  
ecnotopssr  
dikchdnpnb  
bstapleokr  

and the list of words:

    adapting, apace, bombing, cackles, carnal, chump, coccyxes, cowhides, crazies, crumbled, dock, fickler, foaming, guts, knows, lived, minuend, molested, mown, pears, probed, rhubarb, rioted, shinier, solaria, staple, tops, wide, winced

you can find these words:

    apace, cowhides, crazies, dock, knows, lived, mown, pears, probed, rhubarb, rioted, staple, tops, wide

but these are the decoys:

    adapting, bombing, cackles, carnal, chump, coccyxes, crumbled, fickler, foaming, guts, minuend, molested, shinier, solaria, winced

For this puzzle, there are 14 words with a total length of 76 letters. (Some of the words may overlap in the grid, but don't worry about that when counting word lengths in your solution.)
About wordsearches

Words can go in any of the eight directions (up, down, left, right, and diagonals) in a straight line. A letter in the grid can be in more than one word. Words don't wrap around the edges of the grid.

In the example above, the words "lived", "wide" and "staple" are in these positions (two words are diagonal and share a letter).


    ..........
    .......e..
    ....l.d...
    .....i....
    ....w.v...
    .......e..
    ........d.
    ..........
    ..........
    .staple...

The longest word, "cowhides", runs vertically upwards:

    ..........  
    ...s......  
    ...e......  
    ...d......  
    ...i......  
    ...h......  
    ...w......  
    ...o......  
    ...c......  
    ..........  

If there are words present in the grid that aren't in the list of words given, ignore them. For instance, you can see the word "brow" running left to right on the seventh row of the grid, but that doesn't count as a word in this puzzle because "brow" isn't in the list of words you're given.

You're safe to assume that each word in the puzzle is present either zero or one times, never more.
File format

The wordsearch puzzle is given as a text file. The first line of the file is WxH, where W and H are the width and height of the puzzle grid, in characters. The next H lines are the grid, each line being W characters long. Finally, there's an arbitrary number of words to look for, one on each line.

Ignore any trailing or leading blank lines, and any whitespace on a line.

The example puzzle above, a ten by ten grid, would be written to a file as:

10x10  
fhjpamownq  
wsdseuqeev  
ieaeladhcr  
piedtiriah  
rzsiwovspu  
oawhakieab  
browpcfrda  
ecnotopssr  
dikchdnpnb  
bstapleokr  
adapting  
apace  
bombing  
cackles  
carnal  
chump  
coccyxes  
cowhides  
crazies  
crumbled  
dock  
fickler  
foaming  
guts  
knows  
lived  
minuend  
molested  
mown  
pears  
probed  
rhubarb  
rioted  
shinier  
solaria  
staple  
tops  
wide  
winced  

Part 1

Your wordsearch puzzle is given in 10-wordsearch.txt . 

What is the total of the lengths of all the words present in the puzzle?

After you've solved the wordsearch and found all the words you can, you'll have some letters unused in any word. For the example wordsearch, once you've found the words, you're left with this:

    fhj.a....q
    w....uq..v
    i.a....h..
    ..e....i..
    ..........
    ....a.....
    ....p.f...
    ........s.
    .i..h.npn.
    b......okr

The letters remaining in the grid are aaabeffhhhiiijknnoppqqrsuvw. 9 of those letters are vowels. 

Part 2

Your wordsearch puzzle is still given in 10-wordsearch.txt.

How many vowels are left over after solving this puzzle?
