guests = ["Alice", "Bob", "Charlie"]
for guest in guests:
    print(f"Welcome to dinner, {guest}.")

missing_guest = "Charlie"
print(f"{missing_guest} cannot make it.")

new_invited = "Dan"
guests[guests.index(missing_guest)] = new_invited
for guest in guests:
    print(f"Welcome to dinner, {guest}.")