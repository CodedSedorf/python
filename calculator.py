num1 = float( input(" Enter first number "))
operator = input("Enter the arithmetic operation. eg +, *, -, /, //, **, %")
num2 = float( input(" Enter second number "))
result = "Final answer is "

if operator == "+":
  print(result + str( num1 + num2))
elif operator == "-":
  print(result + str( num1 - num2))
elif operator == "*":
  print( result + str(num1 * num2))
elif operator == "/":
  if num2 != 0:
    print( result + str(num1 / num2))
  else:
    print("You can't divide with zero")



elif operator == "**":
  print( result + str(num1 ** num2))


elif operator == "//":
  if num2 != 0:
    print( result + str(num1 // num2))
  else:
    print("Valid second number")


elif operator == "%":
  if num2 != 0:
    print( result + str(num1 % num2))
  else:
    print("Valid second number")