## If you are given three sticks, you may or may not be able to arrange them in a triangle. For example, if one of the sticks is 12 inches long and the other two are 1‐inch‐long, you will not be able to get the short sticks to meet in the middle. For any given three values, there is a simple test to see if it is possible to form a triangle: if any variable is greater than the sum of the other two, then you cannot form a triangle using the three values. Otherwise, you can.  
## a. Write a function named is_triangle that takes three integers as arguments, and that returns True or False, depending on whether you can or cannot form a triangle from sticks with the given lengths. 
## b. Write a function named start_triangle_check that prompts the user to input three stick lengths, converts them to integers, and uses is_triangle to check whether sticks with the given lengths can form a triangle.

def start_triangle_check():
  x = input("enter first stick length - x: ") # get stick length
  y = input("enter second stick length - y: ")
  z = input("enter third stick length - z: ")

  x = int(x) # convert to integer
  y = int(y)
  z = int(z)

  a = is_triangle(x,y,z) # call method 'is_triangle' to check if triangle can be formed 
  
  if (a == True):                 # print the result
    print("Can form a triangle")
  else:
    print("Cannot form a triangle")



def is_triangle(x, y, z):         # method to check if triangle can be formed 
  if(x + y > z and y + z > x and x + z > y): 
    return True
  else:
    return False


start_triangle_check()