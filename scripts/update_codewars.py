import requests

USERNAME = "AdeshWardhe"

user = requests.get(
    f"https://www.codewars.com/api/v1/users/{USERNAME}"
).json()

completed = requests.get(
    f"https://www.codewars.com/api/v1/users/{USERNAME}/code-challenges/completed?page=0"
).json()

rank = user["ranks"]["overall"]["name"]
honor = user["honor"]
kata = completed["totalItems"]

with open("README.md", "r", encoding="utf-8") as file:
    content = file.read()

import re

content = re.sub(
    r'<!--RANK-->.*?<!--/RANK-->',
    f'<!--RANK-->{rank}<!--/RANK-->',
    content
)

content = re.sub(
    r'<!--HONOR-->.*?<!--/HONOR-->',
    f'<!--HONOR-->{honor}<!--/HONOR-->',
    content
)

content = re.sub(
    r'<!--KATA-->.*?<!--/KATA-->',
    f'<!--KATA-->{kata}<!--/KATA-->',
    content
)

with open("README.md", "w", encoding="utf-8") as file:
    file.write(content)

print("Updated!")
