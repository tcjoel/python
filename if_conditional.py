units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    print(num_of_days > 0)
    condition = num_of_days > 0
    print(type(condition))
    if num_of_days > 0:
        return(f"{num_of_days} days are {num_of_days*units} {name_of_unit}")
    elif num_of_days == 0:
        return "your result is 0, please enter a positive number"
    else:
        return "You need to enter a positive entiger!"

user_input = input("Hi, enter a number of days to be convert in hours!\n")
if user_input.isdigit():
    user_input_numb = int(user_input) 
    calculated_value = days_to_units(user_input_numb)
    print(calculated_value)
else:
    print("your input is not a valide number. Don't damage my application!")