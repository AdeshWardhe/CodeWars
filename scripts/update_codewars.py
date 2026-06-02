import requests

USERNAME = "AdeshWardhe"

user = requests.get(
    f"https://www.codewars.com/api/v1/users/{USERNAME}"
).json()

rank = user["ranks"]["overall"]["name"]
honor = user["honor"]

readme_path = "README.md"

with open(readme_path, "r", encoding="utf-8") as file:
    content = file.read()

content = content.replace(
    "<!--RANK-->Loading...<!--/RANK-->",
    f"<!--RANK-->{rank}<!--/RANK-->"
)

content = content.replace(
    "<!--HONOR-->Loading...<!--/HONOR-->",
    f"<!--HONOR-->{honor}<!--/HONOR-->"
)

with open(readme_path, "w", encoding="utf-8") as file:
    file.write(content)

print("README updated successfully")
