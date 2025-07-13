dream_vacation = []
pole_running = True 

while pole_running:
    user_choice = input("Your dream vacation place? ")
    dream_vacation.append(user_choice)
    should_continue = input("Should you pass to another person? ")
    if should_continue == 'no':
        pole_running = False

print("Pole result:")
while dream_vacation:
    print(f"- {dream_vacation.pop()}")