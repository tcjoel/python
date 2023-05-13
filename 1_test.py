#print("list on table " + str(50) +" banana and orange")

#print(f"20 days are {20*24*60} minutes")

## use variable to print
# calculation_to_units = 24*60   #variable
# name_of_unit = "minutes"
# print(f"20 days are {20 * calculation_to_units} {name_of_unit}")
# print(f"35 days are {35 * calculation_to_units} {name_of_unit}")

# # use fonction to print
# calculation_to_units = 24*60   #variable
# name_of_unit = "minutes"
# def days_to_units(num_of_days, custom_message):
#     print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
#     print (custom_message)
# days_to_units(30, "this is nice!")
# days_to_units(365, "very good!")

# # use fonction to print with return value
# calculation_to_units = 24*60   #variable
# name_of_unit = "minutes"
# def days_to_units(num_of_days):
#     return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
#
# user_input = input("Hey guys, entre a number of day to be conver in minutes!\n")
# calculated_value = days_to_units(int(user_input))
# print(calculated_value)

# # fonction with condition to validate user input
# calculation_to_units = 24*60   #variable
# name_of_unit = "minutes"
# def days_to_units(num_of_days):
#     check_var_type = num_of_days > 0
#     print(type(check_var_type))
#     if num_of_days > 0:
#       return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
#     elif num_of_days == 0:
#       return "you enter zero please enter a valide positive number!"
# def validate_execute():
#     if user_input.isdigit():
#         calculated_value = days_to_units(int(user_input))
#         print(calculated_value)
#     else:
#         print("your input is not a valide positive number. Don't ruin my code")
#
# user_input = input("Hey guys, entre a number of day to be conver in minutes!\n")
# validate_execute()

# # fonction with nested if statement to validate user input
# calculation_to_units = 24*60   #variable
# name_of_unit = "minutes"
# def days_to_units(num_of_days):
#       return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
#
# def validate_execute():
#     if user_input.isdigit():
#         if int(user_input) > 0:
#             calculated_value = days_to_units(int(user_input))
#             print(calculated_value)
#         elif int(user_input) == 0:
#                print("you enter zero please enter a valide positive number!")
#     else:
#         print("your input is not a valide positive number. Don't ruin my code")
#
# user_input = input("Hey guys, entre a number of day to be conver in minutes!\n")
# validate_execute()

#fonction with try/except to display nice message when the code crash
calculation_to_units = 24*60   #variable
name_of_unit = "minutes"
def days_to_units(num_of_days):
      return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def validate_execute():
    try:
        if int(user_input) > 0:
             calculated_value = days_to_units(int(user_input))
             print(calculated_value)
        elif int(user_input) == 0:
             print("you enter zero please enter a valide positive number!")
        else:
            print("your input is a negative number, no conversion for you")
    except ValueError:
        print("your input is a negative number. Don't ruin my code")
user_input = input("Hey guys, entre a number of day to be conver in minutes!\n")
validate_execute()