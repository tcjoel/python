import datetime

user_input = input("enter your goal with a dateline separated with a colone like this <goal>:DD.MM.YYYY\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_till = deadline_date - today_date
time_till_days = time_till.days
time_till_hours = int(time_till.total_seconds()/3600)
time_till_second = time_till.total_seconds()
print(today_date)
print(time_till)
print(time_till_days)
print(time_till_hours)
print(time_till_second)

print(f"Dear user! Time remaining for your goal is : {goal} is {time_till}")

## google PYPI to download additional module or package to install in your python,
## Module is a python file with fonctions and variables we need, PACKAGE is a collection of module always whit "_init_.py" file