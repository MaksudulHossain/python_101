buddy = {
    'type': 'dog',
    'owner_name': 'Liam'
}
whiskers = {
    'type': 'cat',
    'owner_name': 'Amina'
}
chewy = {
    'type': 'hamster',
    'owner_name': 'Sofia'
}
goldie = {
    'type': 'fish',
    'owner_name': 'Omer'
}
coco = {
    'type': 'parrot',
    'owner_name': 'Grace'
}

pets = [buddy, whiskers, chewy, goldie, coco]

for pet in pets:
    print("pet description:")
    for k, v in pet.items():
        print(f"{k}: {v}")
    print()

