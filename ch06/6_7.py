person1 = {
    'first_name': 'Moshud',
    'last_name': 'Iqbal',
    'age':36,
    'city':'Dhaka'
}

person2 = {
    'first_name': 'Mamunur',
    'last_name': 'Rshid',
    'age':40,
    'city':'Atlanta'
}

person3 = {
    'first_name': 'Humayun',
    'last_name': 'Ahmed',
    'age':45,
    'city':'Albany'
}

people = [person1, person2, person3]

for person in people:
    print("description:")
    for k, v in person.items():
        print(f"{k}: {v}")
    print()
    
# for k, v in person.items():
#     print(f"{k} = {v}")