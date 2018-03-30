import math
class PaginationHelper:

  # constructor takes in an array of items and a integer indicating
  def __init__(self,data_list , items_per_page):
    self.data_list = data_list
    self.items_per_page = items_per_page
  
  

  # method to return the number of pages
  def page_count(self):
    print('item count',self.item_count())
    print('items per page',self.items_per_page)
    return int(math.ceil( self.item_count() / self.items_per_page))


  # method to return the number[length] of items within the entire array of items
  def item_count(self):
    return len(self.data_list)
  

  # method that returns what page an item is on
  def page_index(self,item_index):
    if item_index < self.item_count() and item_index >= 0 :
      return int(item_index/self.items_per_page)
    return -1           # return -1 for item_index values that are out of range


  # method that returns the number of items on the current page 
  def page_item_count(self, page_index):
    if (page_index+1) * self.items_per_page <= self.item_count():
      return self.items_per_page
    if page_index*self.items_per_page < self.item_count() and (page_index+1) * self.items_per_page > self.item_count():
      return self.item_count() % self.items_per_page
    return -1                   # return -1 for page_index values that are out of range
    

try:
    data_list=[]
    with open("Characters_read.txt") as infile: #open the file to read
      letter = infile.read()
      for i in [',']:  #check for the special characters
          if i in letter: 
            letter = letter.replace(i,"")
      data_list = list(letter)
    infile.close()
    
    helper = PaginationHelper(data_list, 5)
    
    print (helper.page_count())
    print (helper.item_count())
    print (helper.page_item_count(0))
    print (helper.page_item_count(1))
    print (helper.page_item_count(8))
    print (helper.page_index(5))
    print (helper.page_index(2))
    print (helper.page_index(20))
    print (helper.page_index(-10))

except FileNotFoundError: #file not found exception
  print("Couldn't find the file")
except OSError: #file not readable exception
  print("File Found - Problem reading the file")
except SyntaxError: # exception to throw syntax error
  print("SyntaxError")