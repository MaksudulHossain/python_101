favorite_number = {
    'sunny':[7,17],
    'abul':[2,28],
    'jewel':[3,40],
    'shimul':[4,77,98],
    'mishu':[0,1,2]
}

for name, number in favorite_number.items():
    print(f"{name}'s favorite number is {', '.join([str(num) for num in number])}")