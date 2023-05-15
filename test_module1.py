## google PYPI to download additional module, package, dependency or library to install in your python,
## Module is a python file with fonctions and variables we need, PACKAGE is a collection of module always whit "_init_.py" file
## "pip" is package manager for python, it help to install external packages, library or dependency in python
def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days*24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days*24*60} minutes"
    else:
        return "unsupported unit, use hours or minutes "

def validate_execute(days_and_unit_dictionary):
    try:
        if int(days_and_unit_dictionary["days"]) > 0:
             calculated_value = days_to_units(int(days_and_unit_dictionary["days"]), days_and_unit_dictionary["unit"])
             print(calculated_value)
        elif int(days_and_unit_dictionary["days"]) == 0:
             print("you enter zero as number of day. Please enter a valide positive number!")
        else:
            print("your input is not a valide number, no conversion for you")
    except ValueError:
        print("your input is not a valide number. Don't ruin my code")

user_input_message = "Hey guys, entre a number of days and the units of conversion.\nExample 20:hours or 20:minutes to convert 20 days in hours or minutes\n"

# user_input = ""  # to give a first value to our user_input different to "exit". To be able to start the pragram
# while user_input != "exit":  # stop the program is the user_input is "exit"
#     user_input = input("Hey guys, entre a number of days and the units of conversion.\n"
#                        "Example 20:hours or 20:minutes to convert 20 days in hours or minutes\n")
#     days_and_unit = user_input.split(":")
#     days_and_unit_dictionary = { "days":days_and_unit[0], "unit": days_and_unit[1]}
#     print(days_and_unit)
#     print(days_and_unit_dictionary)
#     print(type(days_and_unit_dictionary))
#     validate_execute()
