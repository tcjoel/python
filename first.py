# format
print("12 days give you " + str(12*24*60) + " minutes")
print(f"12 days give you {12*24*60} minutes")

# variable
x=12*24*60
print(x)
a=x/10
print(a)

#fonction
units = 24
name_of_unit = "hours"
def days_to_units():
    print(f"12 days are {12*units} {name_of_unit}")
    print("Nice work")
    
days_to_units()

#fonction parameter (is the input value alocated to fonction)
def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days*units} {name_of_unit}")
    print(custom_message)
    
days_to_units(20, "awsome, I like the result")

#user input and return to fonction
def days_to_units(num_of_days):
    return(f"{num_of_days} days are {num_of_days*units} {name_of_unit}")

my_num = days_to_units(15)
print(my_num)

#
def days_to_units(num_of_days):
    return(f"{num_of_days} days are {num_of_days*units} {name_of_unit}")

user_input = input("Hi, enter a number of days to be convert in hours!\n")
user_input_numb = int(user_input) 
calculated_value = days_to_units(user_input_numb)
print(calculated_value)




