def make_order(*items):
    for item in items:
        print(f"- {item}")

make_order('onions')
make_order('onions', 'green pepper')
make_order('onions', 'green pepper', 'pineapple')