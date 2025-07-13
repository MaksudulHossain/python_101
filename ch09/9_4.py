import restaurant_class2 as res

restaurant = res.Restaurant('Ramna', 'Bangladeshi')
print(restaurant.number_served)
restaurant.number_served = 23
print(restaurant.number_served)
restaurant.set_number_served(100)
print(restaurant.number_served)
restaurant.increment_number_served(10)
print(restaurant.number_served)





