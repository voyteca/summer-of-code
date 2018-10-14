Now you've got the food prepared, it's time to cook it!

Given the numbers you're expecting, you little kettle barbeque won't do. As a special offer with the Mowmaster 5000, you've got yourself a new Inceraptor THX-1138 multifuel outdoor cooking installation.

As you open the box with a sinking heart, contemplating the vast array of parts with just the wrong number of screws, you only hope is the instuction sheet. As Inceraptor produce cutting-edge products (ouch), they have cutting-edge instructions. You fire up your Jaz drive and display the instructions.

They're garbled.

The instructions are given in 05-instructions.txt, as ASCII text.

You take a look at the file and see someone's been tinkering with it by adding comments. Luckily, the comments are easy to spot. A comment starts with a < character and ends with a > character. These two characters and everything within them should be ignored. For example, the line

this is <a comment followed by>some text

should read

this is some text
the comment <a commment followed by> is ignored.

There can be more than one comment on a line, so the line

255 255:4:2<0 166  1>: <00  223 255 :1> 255 255 255 25:13:2
contains two comments, and should end up being

255 255:4:2:  255 255 255 25:13:2
Comments can't be nested. Within a comment, additional < characters are ignored. For example, the line

123 35 > 99 < this should be 35 < 99 > 132 > 54
has a single comment: < this should be 35 < 99 >. Once the comment is removed, the line should be:

123 35 > 99  132 > 54
You can assume that every comment is properly closed. No comment spreads across more than one line: there are no line breaks inside comments.

Part 1
After you've removed all the comments from 05-instructions.txt, how many non-whitespace characters remain in the file? 

("Whitespace characters" are spaces, carriage returns, line feeds, and all that sort of thing. Before you remove comments or anything else, the downloaded instructions contain 165014 non-whitespace characters.)


Even when you've removed all the comments, you can't make sense of the instructions. Then you realise they've been compressed. You'll need to undo the compression in order to view the instructions.

The instructions are compressed with run-length encoding, with colons marking out how fragments were compressed.

In the text abc:2:3:xy, the part :2:3: marks a compression description. This description means the preceeding 2 characters (in this case, bc) were repeated 3 times. In other words, the fragment bc:2:3: represents bcbcbc. This means the uncompressed text should be abcbcbcxyz.

Similarly, 128 255:4:2: means take the four characters preceeding the first colon ( 255) and repeat them twice, meaning the instructions expand to 128 255 255.

Expansion takes place left to right. For instance, with the line

255 255 255 :9:3: 128:9:3:
expansion takes place like this (the instruction being used is underlined):

255 255 255 :9:3: 128:9:3:
            -----

255 255 255  255 255  255 255  128:9:3:
                                  -----
giving

255 255 255  255 255  255 255  128 255  128 255  128
If the expansion starts from the right, things can go wrong. For instance, expanding the same line from the right would give this sequence

255 255 255 :9:3: 128:9:3:
                     -----
                     
255 255 255 :9:3: 128:9:3: 128:9:3: 128
                              -----
                              
255 255 255 :9:3: 128:9:3: 128:9:3: 128:9:3: 128 128
                                       -----
                                       
255 255 255 :9:3: 128:9:3: 128:9:3: 128:9:3: 128:9:3: 128 128 128
                                                -----
                                                
255 255 255 :9:3: 128:9:3: 128:9:3: 128:9:3: 128:9:3: 128:9:3: 128 128 128 128
                                                -----
and so on, forever. Don't expand from the right.

The instructions are stored as a sequence of lines. Each line is compressed separately, so there's no looking back over previous line breaks.

If there aren't enough characters preceeding the expansion instruction, just use all the characters available. For instance, abc:10:2: should be treated the same as abc:3:2:, as there are only three characters before the expansion. Both these strings will expand to abcabc.

Part 2
The instructions are still in 05-instructions.txt, as ASCII text. 

After you've removed all the comments, and then done all the expansion, how many non-whitespace characters remain in the file?

("Whitespace characters" are spaces, tabs, carriage returns, line feeds, and all of that sort of thing.)
