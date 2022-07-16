# we use a "set()" fonction to avoid duplucated value inside our list
# we want to convert number of days in hours or minutes days:minutes or days:hours


def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days*24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days*24*60} minutes"
    else:
        return "unsupported unit"

def validate_and_execute():
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

# run the while loop indefinitly
# while True:

# run the loop util the user enter the value exit, you need to give a first value to the user input
user_input = ""
while user_input != "exit":
    user_input = input("Hi, enter a number of days:units of conversion hours or minutes!\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days":days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute()
