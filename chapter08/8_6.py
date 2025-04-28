def city_country(city, country):
    return f"{city.title()}, {country.title()}"

city_countries = [('dhaka', 'BD'), ('newyork', 'USA'), ('Jeddah', 'Saudi')]
for city, country in city_countries:
    print(city_country(city, country))