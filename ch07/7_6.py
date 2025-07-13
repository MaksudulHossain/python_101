# version 1
'''
is_running = True
while is_running:
    age = input("What is your age: or quit to quit")
    if age!='quit':
        if int(age)<3:
            print("Free")
        elif int(age)<12:
            print("$10")
        else:
            print("$15")
    else:
        is_running = False

# version 2
age = input("What is your age: or quit to quit")
while age != 'quit':
    age = int(age)
    if age<3:
        print("Free")
    elif age<12:
        print("$10")
    else:
        print("$15")
    age = input("What is your age: or quit to quit")
'''
# version 3
while True:
        age = input("What is your age: or quit to quit")
        if age == 'quit':
             break
        else:
            age = int(age)
            if age<3:
                print("Free")
            elif age<12:
                print("$10")
            else:
                print("$15")
