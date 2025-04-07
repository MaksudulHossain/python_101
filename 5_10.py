current_users = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
new_users = ["Zara", "Liam", "Alice", "Bob", "Omar"]
current_users_lowercase = [curr.lower() for curr in current_users]
for newuser in new_users:
    if newuser.lower() in current_users_lowercase:
        print("You need to enter a new user name.")
    else:
        print("User name is available.")

