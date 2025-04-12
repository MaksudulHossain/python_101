rivers = {
    'nile': 'egypt',
    'padma': 'bangladesh',
    'columbia': 'usa' 
}

for river, country in rivers.items():
    print(f"The {river} runs through {country.title() if country!='usa' else country.upper()}")

print("List of rivers:")
for river in rivers:
    print(river)

print("List of countries:")
for country in rivers.values():
    print(country)