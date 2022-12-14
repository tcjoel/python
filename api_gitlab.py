import requests

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
# print(response.text)
# print(response.json())
print(response.json()[0])

my_projects = response.json()
for project in my_projects:
    print(f"Project Name : {project['name']}\n Project Url: {project['web_url']}\n")
