/*
####  Goldbach Conjecture  ####

Goldbach's Conjecture is amongst the oldest and well-known unsolved mathematical problems. In correspondence with Leonhard Euler in 1742, German mathematician Christian Goldbach made a conjecture, which states:
"Every even whole number greater than 2 is the sum of two prime numbers."
Even though it's been thoroughly tested and analyzed and seems to be true, it hasn't been proved yet (thus, remaining a conjecture.)
Create a function that takes a number and returns an array as per the following rules:
___
*) If the given number is odd and greater than two, return an empty array.
*) If the given number is even and greater than two, return an array of two prime numbers whose sum is the given input.
*) Both prime numbers must be the farthest (with the greatest difference).
___



[Examples]

___
goldbachConjecture(1) ➞ []
// The given number is not greater than 2.

goldbachConjecture(7) ➞ []
// The given number is not an even number.

goldbachConjecture(14) ➞ [3, 11]

goldbachConjecture(544) ➞ [3, 541]

goldbachConjecture(4666) ➞ [3, 4663]
_____



[Notes]

Return array in sequence: [smaller, bigger]


[arrays] [logic] [math] [numbers] 



-------------------------------------------------------------------
[Resources]


[No Resources]


*/
//Your code should go here:

