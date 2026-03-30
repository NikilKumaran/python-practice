age = 20

# Basic if
if age >= 18:
    print("Adult")

# if-else
if age > 18:
    print("Eligible")
else:
    print("Not eligible")

# if-elif-else
if age < 18:
    print("Minor")
elif age < 60:
    print("Adult")
else:
    print("Senior")

# Logical operators
if age > 18 and age < 25:
    print("Young adult")

# Even/odd
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")