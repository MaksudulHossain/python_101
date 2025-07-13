# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# •Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# •Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# •Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# •Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.
guests = ["Alice", "Bob", "Charlie"]
for guest in guests:
    print(f"Welcome to dinner, {guest}.")

missing_guest = "Charlie"
print(f"{missing_guest} cannot make it.")

new_invited = "Dan"
guests[guests.index(missing_guest)] = new_invited
for guest in guests:
    print(f"Welcome to dinner, {guest}.")
    
print("I found a bigger dinner table.")
new_guests = ["David", "Emma", "Frank"]
guests.insert(0,"David")
guests.insert(len(guests)//2,"Emma")
guests.append("Frank")
for guest in guests:
    print(f"Welcome to dinner, {guest}")
    
print("I can invite only 2 people for dinner.")
for i in range(len(guests)-2):
    person_popped = guests.pop()
    print(f"{person_popped}, I am sorry, cannot invite you to dinner.")

for guest in guests:
    print(f"{guest}, you are still invited.")

print(guests)

iter = len(guests)
for i in range(iter):
    del guests[0]
print(guests)