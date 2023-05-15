##MODULE is a python file which containt fonctions or variables that you can call into another python file
#import test_module1
# import test_module1  # To import all the module
# import test_module1 as mod #To rename your test_module1 as mod
# from test_module1 import *  # to import everything from the module
## to import just two definitions "validate_execute" and user_input_message
# import logging
from test_module1 import validate_execute, user_input_message
user_input = ""  # to give a first value to our user_input different to "exit". To be able to start the pragram
while user_input != "exit":  # stop the program is the user_input is "exit"
    user_input = input(user_input_message)
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days":days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit)
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_execute(days_and_unit_dictionary)

## Python have some built-in Module like time, os, date, logging ..

# #to print the os
# import os
# print(os.name)

# #to have the log of your applications
# import logging
# logger = logging.getLogger("Main")
# logger.error("Error happened in the app")
