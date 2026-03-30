# Create dictionary
student = {"name": "Rahul", "age": 20}

# Access
print(student["name"])

# Add/update
student["branch"] = "CSE"
student["age"] = 21

# Loop
for key, value in student.items():
    print(key, value)

# Nested dictionary
users = {
    "user1": {"name": "Rahul"},
    "user2": {"name": "Amit"}
}
print(users["user1"]["name"])