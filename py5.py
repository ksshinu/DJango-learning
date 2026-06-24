import json

data = {
    "name": "John",
    "course": "BSc AI & ML"
}

with open("student.json", "w") as file:
    json.dump(data, file, indent=4)

with open("student.json", "r") as file:
    content = json.load(file)
    print(content)