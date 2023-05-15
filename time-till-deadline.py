# this code input a deadling
import datetime

user_input = input("enter your goal with a dealine separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]
print(input_list)

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_till = deadline_date - today_date
days_till = time_till.days
hours_till = int(time_till.total_seconds() / 3600)

print(f"dear user! time remaining for your goal: {goal} is {time_till.days} hours")



