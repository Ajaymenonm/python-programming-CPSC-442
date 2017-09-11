## I have started walking to home at 7:30 AM for the first mile at slow step (8 min:15 sec per mile), then 3 miles at speed (7 min:12 sec per mile), what time do I get home for breakfast? (format output in hh: min) 


start_time = (7*60*60) + (30*60)
slow_step_time = (8 * 60) + 15
fast_step_time = (7 * 60) + 12

total_time = (1 * slow_step_time) + (3 * fast_step_time) # total walk time in seconds for 4 miles

walk_time = (start_time + total_time) / 60 # convert seconds to minutes

hour = walk_time / 60

minutes = walk_time % 60 

eta = "%d hr: %d min" % (hour,minutes) # format output in hh: min

print("estimated time of arrival for breakfast - " +  str(eta))





