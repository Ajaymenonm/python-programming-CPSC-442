import copy
import sys

def logic():   

   rows = int(input("Enter the rows : ")) # user input for rows
   columns = int(input("Enter the columns : "))   # user input for cols

      
   postbox = 'c'
   postboxes = [[postbox for i in range(rows)]]   # multidimensional list

   for j in range (1,columns):    # logic for the postboxe opening
      box = copy.deepcopy(postboxes[j-1])
      box = [element.lower() for element in box]

      for i in range (j,rows,j+1):   
         if(postboxes[j-1][i]=='c' or postboxes[j-1][i]=='C'):  #if previous postbox is close,
            box[i]='O' # the open the box
         else:  
            box[i]='C' # else close the box

      postboxes.append(box)  # append the new updated result in multidimensional list

   for postbox in postboxes:  # print the list in desired output format

      for item in postbox:
         print(item, " | ")
      print()

def continue_prog():   # asking user if he wants to continue.
   choice = input("Do you want to continue?: ")
   
   if (choice.upper()=='Y'):
      main()
   else:
      print("Done")

def main():    # entry point
   logic()  # calling function in main
   continue_prog()    # calling function in main

if __name__ == "__main__": # calling main fuction
    main()
