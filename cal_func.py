#function Addition
def addMe(num1, num2):
  newValue = num1 + num2
  return newValue

#function Subtraction
def subMe(num1, num2):
  newValue = num1 - num2
  return newValue

#function Division
def divMe(num1, num2):
  newValue = num1 / num2
  return newValue

#function Multiplication
def mulMe(num1, num2):
  newValue = num1 * num2
  return newValue

#function exponent
def powerMe(num1, num2):
  newValue = num1 ** num2
  return newValue
#


firstNum = float(input("Enter first number "))
secondNum = float(input("Enter second number "))
operator = input(" Perform basic operation with either +, -, / or * ")

if operator == "+":
  result = addMe(firstNum, secondNum)
  print(f"Your final result is {result} ")
elif operator == "-":
  result = subMe(firstNum, secondNum)
  print(f" Your final result is {result} ")
elif operator == "*":
  result = mulMe(firstNum, secondNum)
  print(f"Your result is {result} ")
elif operator == "/":
  if secondNum == 0:
    print("Sorry, you cannot divide an integer with zero")
  else:
    newResult = divMe(firstNum, secondNum)
    print(f"Your answer is {newResult}")
elif operator == "**":
  newResult = powerMe(firstNum, secondNum)
  print(f"Your final result is {newResult} ")