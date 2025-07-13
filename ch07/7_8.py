sanwitch_orders = ['tuna', 'pastrami', 'chicken', 'pastrami', 'beef', 'pastrami', 'veggie']
finished_sandwitches = []
while sanwitch_orders:
    current = sanwitch_orders.pop()
    print(f"I made your {current} sandwitch")
    finished_sandwitches.append(current)

for item in finished_sandwitches:
    print(item)

