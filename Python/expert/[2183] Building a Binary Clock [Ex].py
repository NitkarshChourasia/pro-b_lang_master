"""
####  Building a Binary Clock  ####

A binary clock displays the time of day in binary format. Modern binary clocks have six columns of lights; two for each of the hours, minutes and seconds. The photo below shows a binary clock displaying the time "12:15:45":

The binary values increase from the bottom to the top row. Lights on the bottom row have a value of 1, lights on the row above have a value of 2, then 4 on the row above that, and finally a value of 8 on the top row. Any 24-hour time can be shown by switching on a certain combination of lights. For example, to show the time "10:37:49":

You've decided to build your own binary clock, and you need to figure out how to light each row of the clock to show the correct time. Given the time as a string, return a list containing strings that shows the lights for each row of the clock (top to bottom). Use "1" for on, and "0" for off. Leave a blank space for any part of the row that doesn't require a light.


[Examples]

___
binary_clock("10:37:49") ➞ [
  " 0 0 1",
  " 00110",
  "001100",
  "101101"
]

binary_clock("18:57:31") ➞ [
  " 1 0 0",
  " 01100",
  "000110",
  "101111"
]

binary_clock("10:50:22") ➞ [
  " 0 0 0",
  " 01000",
  "000011",
  "101000"
]
_____



[Notes]

See the Resources section for more information on binary clocks.


[arrays] [strings] 



-------------------------------------------------------------------
[Resources]
_________
How to obtain the binary representation of an integer in Python?
https://www.decalage.info/python/int2binary
Converting to binary using str.format().
_________
_________
Binary Clock
https://en.wikipedia.org/wiki/Binary_clock
A clock that displays the time of day in a binary format. Originally, such clocks showed each decimal digit of sexagesimal time as a binary value, but presently binary …
_________
_________
bin() Method
https://www.programiz.com/python-programming/methods/built-in/bin
Converts and returns the binary equivalent string of a given integer. If the parameter isn't an integer, it has to implement __index__() method to return an integer.
_________

"""
#Your code should go here:

