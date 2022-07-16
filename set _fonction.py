# we use a "set()" fonction to avoid duplucated value inside our list

units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return(f"{num_of_days} days are {num_of_days*units} {name_of_unit}")

def validate_and_execute():
    try:
        user_input_numb = int(num_of_days_element)
        if user_input_numb > 0:
            calculated_value = days_to_units(user_input_numb)
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
    user_input = input("Hi, enter a number of days to be convert in hours!\n")
    list_of_days = user_input.split(", ")
    print(set(list_of_days))
    print(list_of_days)
    
    print(type(set(list_of_days)))
    print(type(list_of_days))
# let's use the set fonction
    for num_of_days_element in set(user_input.split(", ")):
        validate_and_execute()