sandwitch_orders = ['tuna', 'pastrami', 'chicken', 'pastrami', 'beef', 'pastrami', 'veggie']
finished_sandwitches = []
print("The deli has run out of pastrami")

while "pastrami" in sandwitch_orders:
    sandwitch_orders.remove("pastrami")

for sandwitch in sandwitch_orders:
    finished_sandwitches.append(sandwitch)

print(finished_sandwitches)