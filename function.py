#Creating Functions

# def sedorf():
#   text = "Hello Jomiloju boy"
#   text1 = "How are you today,"
#   text3 = "Have you eaten?"
#   print(f" {text}. {text1} and {text3}.")

# sedorf()

#Function with argument
def Sedorf(quote):
  print(quote)
  print(quote)
  print(quote)

Sedorf("Constant practice makes notable success.")


#Functions plus if statement
def sch_age_calculator(age, name):
  if age < 5:
    print(f" Enjoy the time! {name} is only {age} years and cannot start school yet.")
  elif age == 5:
    print("Congratulation", name, "you have been admitted in the kindergarten class.")
  else:
    print(name, "is too old to be in the kindergarten.")

sch_age_calculator(5, "Sedorf")


#another function (Maybe I will call it reusable function)
def add_ten_to_age(age):
  new_age = age + 15
  return new_age


myAge = add_ten_to_age(25)
print(myAge)

jomiloju_age_in_15_years = add_ten_to_age(15)
print(jomiloju_age_in_15_years)