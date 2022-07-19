# we use the fonction import
# import module
# using the "import" to call this module in you code like this "module.validate_and_execute()"

# to import a specific fonction or variable from a module named "module"
# when you use the "from" syntax, you don't need to call the module in your code
# your can type "from module * "" to import all the module with the
from module import validate_and_execute, user_input_message

user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days":days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute(days_and_unit_dictionary)

