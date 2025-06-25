# while loop
# x = 0 
# while (x<9):
#   print(x)
#   x = x+1


# y = 12
# while y < 25:
#   print(y)
#   y = y + 1

#for loop
# for x in range(5, 11):
#   print(x)
#List
days = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]

# #Printing list
for items in days:
  if(items == "Wed" and items == "Fri"):continue
  print(items)

# #dictionary
# student_details = {
#   "food": "Rice",
#   "age": 19,
#   "subject": "Python"
# }
# # Print only the food
# print(student_details["food"])   # Output: Rice
# #Printing dictionary
# for key, value in student_details.items():
#   print(f"{key}: {value}")




#List of dictionaries
teachers_in_sch = [
  {"name": "Diekoloreoluea", "age": 14, "subject": "English"},
  {"name": "Sedorf", "age": 55, "subject": "Maths"},
  {"name": "Ola", "age": 25, "subject": "Coding"},
  {"name": "Bola", "age": 19, "subject": "Chemistry"},
]
#Printing list of dictionary
for teachers in teachers_in_sch:
  if (teachers == "Sedor"): break
  print(teachers)
#Printing just one teacher from list of dictionary
# for only_names in teachers_in_sch:
#     print(only_names["name"])
