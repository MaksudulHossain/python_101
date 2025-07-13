bike = [
    "Honda CBR500R",
    "Yamaha YZF-R3",
    "Kawasaki Ninja 400",
    "Suzuki GSX-R600",
    "Royal Enfield Classic 350"
]

print(bike)

bike.append('yamaha')

bike.insert(2, 'toyota')

print(bike)

# del bike[5]
del bike[bike.index('yamaha')]
popped_val = bike.pop()
print(popped_val)

bike.remove('Kawasaki Ninja 400') #if multiple times, the first one will get removed, cons if I cannot remove completely

print(bike)

