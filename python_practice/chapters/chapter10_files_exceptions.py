# Write file
with open("file.txt", "w") as f:
    f.write("Hello")

# Read file
with open("file.txt") as f:
    print(f.read())

# Exception handling
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

# File exception
try:
    with open("missing.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")