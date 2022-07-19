# Module is a python file that content fonction or variable that you can use in an other python file
def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days*24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days*24*60} minutes"
    else:
        return "unsupported unit"

def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_numb = int(days_and_unit_dictionary["days"])
        if user_input_numb > 0:
            calculated_value = days_to_units(user_input_numb, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_numb == 0:
            print("your result is 0, please enter a positive number")
        else:
            print("you entered a negative value, no conversion for you")
    except ValueError:
        print("your input is not a valide number. Don't damage my application!")
user_input_message = "Hi, enter a number of days:units of conversion hours or minutes!\n"
