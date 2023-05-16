#!/bin/python
## pip install pyyaml
##

import csv
import os

import random
import yaml

  ## To read YAML file
# dir_path = os.path.dirname(os.path.realpath(__file__))

# with open("dev/test2.yml", "r") as f:
#     data = yaml.safe_load(f)
#     print(data)
#     print(type(data))
#     # contents[]
#     # print(PWD)
#     # print(list(contents))
#     # print(type(contents))

   ## to play a random game
# with open("test_game.yaml", "r") as f:
#     config = yaml.safe_load(f)
# range_min = config['range']['min']
# range_max = config['range']['max']
# guesses_allowed = config['guesses']
# mode = config['mode']
#
# solved = False
#
# if mode == "single":
#     correct_number = random.randint(range_min, range_max)
# elif mode == "multi":
#     correct_number = int(getpass.getpass("Player 2, please enter the number to guess: "))
# else:
#     print("Invalid config")
#     exit()
#
# for i in range(guesses_allowed):
#     guess = int(input("Enter your guess: "))
#     if guess == correct_number:
#         print (f"Correct! Your needed{i + 1} tries!")
#         solved = True
#         break
#     elif guess < correct_number:
#         print("Too low!")
#     else:
#         print("Too high!")
# if not solved:
#         print("You lost. The number was", correct_number)

  ## To write YAML file

data = {
    "name": "Mike",
    "age": 25,
    "languages": ["Python", "C", "Java"],
    "address": {
        "city": "NYC",
        "ZIP": "1234",
        "country": "US"
    }
}

with open("somefile.yaml" , "w") as f:
    yaml.dump(data, f, default_flow_style=False)