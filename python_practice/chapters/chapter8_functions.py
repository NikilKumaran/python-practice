# Simple function
def greet():
    print("Hello")

greet()

# Function with parameter
def greet_user(name):
    print(f"Hello {name}")

greet_user("Rahul")

# Default parameter
def greet_default(name="Guest"):
    print(name)

greet_default()

# Return value
def add(a, b):
    return a + b

print(add(2, 3))