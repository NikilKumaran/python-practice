# Input
name = input("Enter your name: ")
print("Hello", name)

# While loop
count = 1
while count <= 3:
    print(count)
    count += 1

# Break
while True:
    msg = input("Type 'quit' to exit: ")
    if msg == "quit":
        break