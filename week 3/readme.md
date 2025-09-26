## Python Classes

1. Define a class which has at least two methods:
`getString`: to get a string from console input
`printString`: to print the string in upper case.

2. Define a class named `Shape` and its subclass `Square`. The `Square` class has an `init` function which takes a `length` as argument. Both classes have a `area` function which can print the area of the shape where Shape's area is 0 by default.

3. Define a class named `Rectangle` which inherits from `Shape` class from task 2. Class instance can be constructed by a `length` and `width`. The `Rectangle` class has a method which can compute the `area`.

4. Write the definition of a Point class. Objects from this class should have a
    - a method `show` to display the coordinates of the point
    - a method `move` to change these coordinates
    - a method `dist` that computes the distance between 2 points

5. Create a bank account class that has attributes `owner`, `balance` and two methods `deposit` and `withdraw`. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
```python
class Account:
    pass
```

6. Write a program which can filter prime numbers in a list by using `filter` function.
Note: Use `lambda` to define anonymous functions.

## Python Function

1. A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. 
`ounces = 28.3495231 * grams`

2. Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion:
`C = (5 / 9) * (F – 32)`

3. Write a program to solve a classic puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
`create function: solve(numheads, numlegs):`

4. You are given list of numbers separated by spaces. Write a function `filter_prime` which will take list of numbers as an agrument and returns only prime numbers from the list.

5. Write a function that accepts string from user and print all permutations of that string.

6. Write a function that accepts string from user, return a sentence with the words reversed.
`We are ready -> ready are We`

7. Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
```python
def has_33(nums):
    pass

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
```

8. Write a function that takes in a list of integers and returns True if it contains `007` in order
```python
def spy_game(nums):
    pass

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False
```
9. Write a function that computes the volume of a sphere given its radius.

10. Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection `set`.

11. Write a Python function that checks whether a word or phrase is `palindrome` or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam

12. Define a functino `histogram()` that takes a list of integers and prints a histogram to the screen. For example, `histogram([4, 9, 7])` should print the following:
```
****
*********
*******
```

13. Write a program able to play the `"Guess the number"` - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
``` 
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
```

14. Create a python file and import some of the functions from the above 13 tasks and try to use them.


## Python Function

```python
# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
```

1. Write a function that takes a single movie and returns `True` if its IMDB score is above 5.5

2. Write a function that returns a sublist of movies with an IMDB score above 5.5.

3. Write a function that takes a category name and returns just those movies under that category.

4. Write a function that takes a list of movies and computes the average IMDB score.

5. Write a function that takes a category and computes the average IMDB score.