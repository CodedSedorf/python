#Operators: +(addition), -(subtraction), /(division), *(multiplication), //(whole num which ignores remainer), %(remainder), **(power)
# print("Hello Jomiloju")
# print(15//2)
# print(15/2)
# print(51%2)

#Variable Naming
#Must contains letters, numbers, or underscores
#Should not start with a number
#Spaces are not allowed
#Cannot be keywords (e.g. break, try)
#Short & descriptive are best
#Case sensitive


# red_bucket = "Sedorf"
# print(type(red_bucket))
# red_bucket = 15
# #del red_bucket
# print(type(red_bucket))

#input
# firstName = input("Enter first name")
# lastName = input("Enter lastname")
# print(firstName + " " + lastName  + "is five years old.")

#equality
# age = 13
# price = "13"
# print(age == price)


# uniAge = 18
# jomiloju = 14
# secondarySch = 14
# if jomiloju == uniAge:
#   print("You've been admitted to the University")
# elif jomiloju > secondarySch:
#   print("Enrol for A Level programme")
# else:
#   print("You're to be in secondary school")



num1 = float(input( "Enter first number") )
num2 = float( input("Enter second number") )
signOperator = input("Enter any arithmetic sign. eg +, *, -, /, **")
result = "Answer:"

if signOperator == "+" :
  print( result + str(num1 + num2))
  
