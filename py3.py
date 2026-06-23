try:
    with open("py2.py", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")