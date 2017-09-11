## The cover price of a book is $25, but bookstores get a 10% discount. Shipping costs $2 for the first five copies and 2.75 cents for all rest of copies. Write a Python program to show what is the total wholesale cost for 40 copies display the result. 

cover_price = 25
discount_given = 0.10
shipping_cost_five = 2
shipping_cost_rest = 0.0275

discounted_price = cover_price - (cover_price * discount_given) # calculate the price after discount

total_shipping_cost = (shipping_cost_five * 5) + (shipping_cost_rest * 35) # calculate shipping for 40 copies

wholesale_price = (40 * discounted_price) + total_shipping_cost # calculate wholesale price of 40 books

print("wholesale price for 40 books is " + str(wholesale_price))


