## Write a Python code to calculate the speed for running a 10-kilometer race in 1 hours 5 minutes 42 seconds. What is the average pace (time per mile in minutes and seconds)?  What is the average speed in miles per hour?  


total_time = (1*60*60) + (5*60) + 42

time_for_one_mile = total_time / 6.21371 # in seconds

minute = time_for_one_mile / 60

second = time_for_one_mile % 60

pace = "%dm:%02ds" % (minute,second) 

average_speed = 3600 * 6.21371 / 3942 # calculate average speed


print("average pace: " + str(pace))
print("average speed: " + str(round(average_speed, 2)) + " mph")
