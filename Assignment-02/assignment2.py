## You have just recently been hired to calculate scores for a Dart Board game! Write a function  scoreThrows() that accepts any number of radiuses  (can be integers), and returns a total score using the below specification. 
## Scoring specifications: 
# 0 points ‐ radius above 10 
# 5 points ‐ radius between 5 and 10 inclusive 
# 10 points ‐ radius less than 5 
# If all radiuses are less than 5, award 100 BONUS POINTS! 
# An empty input should return 0. 
## Expected Output: 
# scoreThrows() => returns 0 
# scoreThrows(1, 5, 11) => returns 15 
# scoreThrows(15, 20, 30) => returns 0 
# scoreThrows(1, 2, 3, 4) => returns 140 
# scoreThrows(1, 2, 3, 4, 5, 6, 7, 8, 9) => returns 65

import sys

def scoreThrows(*arg):

  zero_points = 0 # set initial counter to zero
  five_points = 0
  ten_points = 0
  bonus = 0

  for x in arg:
    length_of_array = len(x) # get argument length 

    for y in x:
      y = int(y)

      if (y > 10):           # check various conditions and increment corresponding counter
        zero_points += 1
      elif (y >= 5 and y <= 10):
        five_points += 1
      elif (y < 5):
        ten_points += 1
  
      if (length_of_array == ten_points):
        bonus += 1

    total = (zero_points * 0) + (five_points * 5) + (ten_points * 10) + (bonus * 100) # calculate total

    print("total points: ", total)

scoreThrows(sys.argv[1:]) # get arguments from command line
