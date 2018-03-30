def wordcount():       
   try:
      wordcount = {} # initialize empty hash

      with open("File_to_be_read_relatedto_Assignment_3.1.txt") as file: # open file to read
         for word in file.read().split():   # iterate through through each split word in the file
            
            if word not in wordcount:  # count each word in file
               wordcount[word] = 1      
            else:
               wordcount[word] += 1    # increment the counter

      file.close();  #close the file

      with open("output1.txt","w") as Text_file: # open new file
         for i in wordcount.items(): # iterate through items in hash

            Text_file.write(str(i)+'\n') # write to output file
         
         Text_file.close(); # close the output file.
      
   except FileNotFoundError:  # catch errors
      print("file not found")

   except OSError:    
      print("problem reading from file")


wordcount()   #call the method
