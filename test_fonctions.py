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

# # fonction with CONDITION to validate user input
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

# # fonction with NESTED-IF statement to validate user input
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

# #fonction with TRY/EXCEPT to display nice message when the code crash
# calculation_to_units = 24*60   #variable
# name_of_unit = "minutes"
# def days_to_units(num_of_days):
#       return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
#
# def validate_execute():
#     try:
#         if int(user_input) > 0:
#              calculated_value = days_to_units(int(user_input))
#              print(calculated_value)
#         elif int(user_input) == 0:
#              print("you enter zero please enter a valide positive number!")
#         else:
#             print("your input is not a valide number, no conversion for you")
#     except ValueError:
#         print("your input is not a valide number. Don't ruin my code")
# user_input = input("Hey guys, entre a number of day to be conver in minutes!\n")
# validate_execute()

# #fonction with WHILE-LOOP
# calculation_to_units = 24*60   #variable
# name_of_unit = "minutes"
# def days_to_units(num_of_days):
#       return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
#
# def validate_execute():
#     try:
#         if int(user_input) > 0:
#              calculated_value = days_to_units(int(user_input))
#              print(calculated_value)
#         elif int(user_input) == 0:
#              print("you enter zero please enter a valide positive number!")
#         else:
#             print("your input is not a valide number, no conversion for you")
#     except ValueError:
#         print("your input is not a valide number. Don't ruin my code")
#
# # while True:  # this condition will be always true and live your app up and running
#
# user_input = ""  # to give a first value to our user_input different to "exit". To be able to start the pragram
# while user_input != "exit":  # stop the program is the user_input is "exit"
#     user_input = input("Hey guys, entre a number of day to be conver in minutes!\n")
#     validate_execute()

#fonction with FOR-LOOP
# calculation_to_units = 24*60   #variable
# name_of_unit = "minutes"
# def days_to_units(num_of_days):
#       return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
#
# def validate_execute():
#     try:
#         if int(num_of_days_element) > 0:
#              calculated_value = days_to_units(int(num_of_days_element))
#              print(calculated_value)
#         elif int(num_of_days_element) == 0:
#              print("you enter zero please enter a valide positive number!")
#         else:
#             print("your input is not a valide number, no conversion for you")
#     except ValueError:
#         print("your input is not a valide number. Don't ruin my code")
#
# # while True:  # this condition will be always true and live your app up and running
#
# user_input = ""  # to give a first value to our user_input different to "exit". To be able to start the pragram
# while user_input != "exit":  # stop the program is the user_input is "exit"
#     user_input = input("Hey guys, entre a number of day to be conver in minutes!\n")
#     print(type(user_input.split(", ")))
#     print(user_input.split(", "))
#     for num_of_days_element in user_input.split(", "):
#        validate_execute()


# # LIST of elements
# my_list = [ "8", "test", "0"]
# print(my_list[1])
# my_list.append("good") # to add the element "good" to a list
# my_list.remove("good") # to remove the element "good" from the list
# print(my_list)
# print(my_list[3])


# # SET of element is a list where every element are uniq, the fonction "set(<list_Name>)" is used to change list into set
## {"1", "0", "good"}
# # in a set we can't access element like in the list, we need to use the loop
# # my_set.add("joy") is a way to add element in the set, set is no order
# # my_set.remove("good") # to remove the element "good" from the set
# calculation_to_units = 24*60   #variable
# name_of_unit = "minutes"
# def days_to_units(num_of_days):
#       return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
#
# def validate_execute():
#     try:
#         if int(num_of_days_element) > 0:
#              calculated_value = days_to_units(int(num_of_days_element))
#              print(calculated_value)
#         elif int(num_of_days_element) == 0:
#              print("you enter zero please enter a valide positive number!")
#         else:
#             print("your input is not a valide number, no conversion for you")
#     except ValueError:
#         print("your input is not a valide number. Don't ruin my code")
#
# # while True:  # this condition will be always true and live your app up and running
#
# user_input = ""  # to give a first value to our user_input different to "exit". To be able to start the pragram
# # while user_input != "exit":  # stop the program is the user_input is "exit"
# #     user_input = input("Hey guys, entre a number of day to be conver in minutes!\n")
# #     print(type(set(user_input.split(", "))))
# #     print(set(user_input.split(", ")))
# #     for num_of_days_element in set(user_input.split(", ")):
# #        validate_execute()
# user_input = ""  # to give a first value to our user_input different to "exit". To be able to start the pragram
# # while user_input != "exit":  # stop the program is the user_input is "exit"
#     user_input = input("Hey guys, entre a number of day to be conver in minutes!\n")
#     list_of_day = user_input.split(", ")
#     print(list_of_day)
#     print(set(list_of_day))
#     print(type(list_of_day))
#     print(type(set(list_of_day)))
#     for num_of_days_element in set(user_input.split(", ")):
#        validate_execute()

## some python buit-in fonction
# print("Hello World")
# input("type your name here!\n") # ask for a value that will be added into a variable
# set([1, 5, 5]) # to transform a list into a set
# int("20")  # to transform a string in integer
# "2, 4".split(", ") #fonction call on the value or variable
# [1, 3, 5].count()

# DICTIONARY {"day": 20, "unit": "hours" }
def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days*24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days*24*60} minutes"
    else:
        return "unsupported unit, use hours or minutes "

def validate_execute():
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
user_input = ""  # to give a first value to our user_input different to "exit". To be able to start the pragram
while user_input != "exit":  # stop the program is the user_input is "exit"
    user_input = input("Hey guys, entre a number of days and the units of conversion.\n"
                       "Example 20:hours or 20:minutes to convert 20 days in hours or minutes\n")
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = { "days":days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit)
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_execute()