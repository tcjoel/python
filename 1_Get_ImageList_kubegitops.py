import csv
import yaml
import os

environment = "aws-st2-g"

dir_path = os.path.dirname(os.path.realpath(__file__))
directory = dir_path + "/" + environment
output_csv = dir_path + "/" + environment + "_image_tag.csv"

## Write a list of image name and tag number
with open(output_csv, 'w', newline='') as csvfile:
    fwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for filename in os.listdir(directory):
        fn = os.path.join(directory, filename)
        if os.path.isfile(fn):
            try:
                with open(fn, "r") as stream:
                    data = yaml.safe_load(stream)
                    app_name = data["spec"]["chart"]["name"]
                    tag_number = data["spec"]["values"]["image"]["tag"]
                fwriter.writerow([app_name, tag_number])
            except:
                print(f'chart info not found in file: {filename}')