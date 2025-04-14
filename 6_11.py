citiees = {
    'dhaka':{
        'country':'bangladesh',
        'population':'10.3M',
        'fact': 'most beautiful city in the word'
    },
    'portland':{
        'country':'USA',
        'population':'2.5M',
        'fact': 'City of Roses'
    },
    'makka':{
        'country':'Saudi Arabia',
        'population':'2.4M',
        'fact': 'Qaba is situated'
    }
}

for city, info in citiees.items():
    print(f"{city}:")
    for k, v in info.items():
        print(f"\t{k}:{v}")