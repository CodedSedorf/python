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

firstNum = float(input("Enter first number "))
secondNum = float(input("Enter second number "))
operator = input(" Perform basic operation with either +, -, / or *")

if operator == "+":
  result = addMe(firstNum, secondNum)
  print(f"Your final result is {result}")