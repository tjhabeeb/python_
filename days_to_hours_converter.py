# Creating the variables
calculations_to_units = 24
name_of_unit = "hours"

# Defining the function
def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculations_to_units} {name_of_unit}"
    elif num_of_days == 0:
        return "You entered a 0, please enter a positive number"
    else:
        return "This is an invalid number"

# Updated validate_and_execute function with parameter
def validate_and_execute(user_input):
    if user_input.strip().isdigit():
        user_input_number = int(user_input)
        result = days_to_units(user_input_number)
        print(result)
    else:
        print("You entered an invalid value, please enter a positive integer")

# Main input loop
user_input = ""
while user_input.lower() != "exit":
    user_input = input("Enter a number of days (comma-separated if multiple), or 'exit' to quit: ")
    if user_input.lower() == "exit":
        break
    for num_of_days_element in user_input.split(","):
        validate_and_execute(num_of_days_element)
