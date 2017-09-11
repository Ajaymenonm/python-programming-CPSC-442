## The Hidden Word: Maya writes weekly articles for a well‐known magazine, but she is missing one word each time she is about to send the article to the editor. The article is not complete without this word. Maya has a friend, Dan, and he is very good with words, but he does not like just to give them away. He texts Maya a number, and she needs to find out the hidden word. 

# The words can contain only the letters: 
#  "a", "b", "d", "e", "i", "l", "m", "n", "o", and "t". 

# Luckily, Maya has the key: 
# "a" – 6, "b" – 1, "d" – 7, "e" – 4, "i" – 3, "l" – 2, "m" – 9, "n" – 8, "o" – 0, and "t" – 5 

# Write a function  hidden(num) which accepts number and returns the hidden‐word which is missing. 


input_number = input('enter the value: ') # get the number from command line
  
def hidden(num):
  num_array = map(int, str(num)) # strip number to digits
  decoded_word = ""

  for i in num_array:

    KEY = {      # dictionary
        6: "a",
        1: "b",
        7: "d",
        4: "e",
        3: "i",
        2: "l",
        9: "m",
        8: "n",
        0: "o",
        5: "t",
    }

    decoded_word += KEY[i] # form decoded string

  print(decoded_word)

hidden(input_number)