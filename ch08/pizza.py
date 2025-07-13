def make_pizza(size, *toppings):
    print(f"Making a {size} pizza folloing toppings: ")
    for topping in toppings:
        print(f"- {topping}")

if __name__ == '__main__':
    print("I am running from main...")
    make_pizza(11, 'onions', 'garlic')
