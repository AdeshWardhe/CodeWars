import requests
import re

USERNAME = "AdeshWardhe"

# Fetch user stats
user = requests.get(
    f"https://www.codewars.com/api/v1/users/{USERNAME}"
).json()

# Fetch completed challenges
completed = requests.get(
    f"https://www.codewars.com/api/v1/users/{USERNAME}/code-challenges/completed?page=0"
).json()

# Extract data
rank = user["ranks"]["overall"]["name"]
honor = user["honor"]
kata = completed["totalItems"]

# Progress bar calculation
goal = 100

percent = min(int((kata / goal) * 100), 100)

filled = percent // 10
empty = 10 - filled

progress_bar = "🟩" * filled + "⬜" * empty + f" {percent}%"

# Read README
with open("README.md", "r", encoding="utf-8") as file:
    content = file.read()

# Update Rank
content = re.sub(
    r'<!--RANK-->.*?<!--/RANK-->',
    f'<!--RANK-->{rank}<!--/RANK-->',
    content
)

# Update Honor
content = re.sub(
    r'<!--HONOR-->.*?<!--/HONOR-->',
    f'<!--HONOR-->{honor}<!--/HONOR-->',
    content
)

# Update Kata Count
content = re.sub(
    r'<!--KATA-->.*?<!--/KATA-->',
    f'<!--KATA-->{kata}<!--/KATA-->',
    content
)

# Update Progress Bar
content = re.sub(
    r'<!--PROGRESS-->.*?<!--/PROGRESS-->',
    f'<!--PROGRESS-->\n{progress_bar}\n<!--/PROGRESS-->',
    content,
    flags=re.DOTALL
)

# Save README
with open("README.md", "w", encoding="utf-8") as file:
    file.write(content)

print("README updated successfully!")
