units = 24
name_of_unit = "hours"

#### Try except or try catched is use to avoid the error message "ValueError" should in case you miss something
# def days_to_units(num_of_days):
#     return(f"{num_of_days} days are {num_of_days*units} {name_of_unit}")

# def validate_and_execute():
#     try:
#         user_input_numb = int(user_input)
#         if user_input_numb > 0:
#             calculated_value = days_to_units(user_input_numb)
#             print(calculated_value)
#         elif user_input_numb == 0:
#             return "your result is 0, please enter a positive number"
#         else:
#             return "you enter a negative number, there is no calculation for you"
#     except ValueError:
#         print("your input is not a valide number. Don't damage my application!")
        
# user_input = input("Hi, enter a number of days to be convert in hours!\n")
# validate_and_execute()

def days_to_units(num_of_days):
    return(f"{num_of_days} days are {num_of_days*units} {name_of_unit}")

def validate_and_execute():
    if user_input.isdigit():
        user_input_numb = int(user_input)
        if user_input_numb > 0:
            calculated_value = days_to_units(user_input_numb)
            print(calculated_value)
        elif user_input_numb == 0:
            return "your result is 0, please enter a positive number"
    else:
        print("your input is not a valide number. Don't damage my application!")
        
user_input = input("Hi, enter a number of days to be convert in hours!\n")
validate_and_execute()