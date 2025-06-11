#creating the variables
calculations_to_units = 24
name_of_unit = "hours"

#defining the function
def days_to_units(num_of_days):
  
  if num_of_days > 0:
   return f"{num_of_days} days are {num_of_days * calculations_to_units} {name_of_unit}"
  elif num_of_days == 0:
   return "You entered a 0, please enter a positive number"
  else:
   return "This is an invalid number"
 
  
  


def validate_and_execute():
 if user_input.isdigit():
   user_input_number = int(user_input)
   calculated = days_to_units(int(user_input_))
   print(calculated)
 else:
  print("You entered an invalid value, please enter an integer")


user_input = ""
while user_input != "exit":
  user_input = input("Enter a number of days: ")
  for num_of_days_element in user_input.split(","):
   validate_and_execute()






