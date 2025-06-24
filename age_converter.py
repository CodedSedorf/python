user_age = float(input(" Enter your age "))
show_age = input(" show my age in days, hours, minutes or seconds ").lower()

if show_age == "day" or show_age == "days":
  #calculating age in days
  result_in_days = user_age * 365
  print( " Your age in days is " + str(result_in_days))
elif show_age == "hour" or show_age == "hours":
  #calculating in hours
  result_in_hours = user_age * 365 * 24
  print(" Your age in hours is " + str(result_in_hours))
elif show_age == "minute" or show_age == "minutes":
  #calculating age in minutes
  result_in_minutes = user_age * 365 * 24 * 60
  print(" Your age in minutes is " + str(result_in_minutes))
elif show_age == "second" or show_age == "seconds":
  #calculating age in seconds
  result_in_seconds = user_age * 365 * 24 * 60 * 60
  print(" Your age in seconds is " + str(result_in_seconds))
elif show_age == "days" or show_age == "day" and show_age == "hour" or show_age == "hours" and show_age == "minute" or show_age == "minutes" and show_age == "second" or show_age == "seconds":
  resDays = user_age * 365
  resHrs = user_age * 365 * 24
  resMins = user_age * 365 * 24 * 60
  resSecs = user_age * 365 * 24 * 60 * 60 
  print(" Your age in days, hours, minutes and seconds is " + str(resDays) + str(resHrs) + str(resMins) + str(resSecs)) 