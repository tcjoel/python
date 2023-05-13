import sys
#import requests
import re
import csv
import yaml
import os
from pprint import pprint

environment = "st2"

dir_path = os.getcwd()
dir_path = os.path.dirname(os.path.realpath(__file__))
directory = dir_path + "/" + environment
output_csv = dir_path + "/" + environment + "_chart_versions.csv"
final_output_csv = dir_path + "/" + environment + "_chart_versions_inMuseum.csv"

## find all charts/versions
with open(output_csv, 'w', newline='') as csvfile:
    fwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    #fwriter.writerow(["chart_name", "version"])

    for filename in os.listdir(directory):
        fn = os.path.join(directory, filename)
        if os.path.isfile(fn):
            try:
                with open(fn, "r") as stream:
                    data = yaml.safe_load(stream)
                    app_name = data["spec"]["chart"]["name"]
                    version = data["spec"]["chart"]["version"]
                fwriter.writerow([app_name, version,"?"])
            except:
                print(f'chart info not found in file: {filename}')
