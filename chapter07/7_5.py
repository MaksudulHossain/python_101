while True:
    age = int(input("What is your age: "))
    if age<3:
        print("Free")
    elif age<12:
        print("$10")
    else:
        print("$15")
    choice = input("What to continue? y/n? ")
    if choice == 'n':
        break 


