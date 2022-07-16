units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return(f"{num_of_days} days are {num_of_days*units} {name_of_unit}")

def validate_and_execute():
    if user_input.isdigit():
        user_input_numb = int(user_input)
        if user_input_numb > 0:
            calculated_value = days_to_units(user_input_numb)
            print(calculated_value)
        elif user_input_numb == 0:
            print("your result is 0, please enter a positive number")
    else:
        print("your input is not a valide number. Don't damage my application!")

# run the while loop indefinitly
# while True:

# run the loop util the user enter the value exit, you need to give a first value to the user input
user_input = ""
while user_input != "exit":
    user_input = input("Hi, enter a number of days to be convert in hours!\n")
    validate_and_execute()