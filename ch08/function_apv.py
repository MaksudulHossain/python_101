
def greet(myname):
    name = myname
    counter = 0
    while True:
        if counter == 10:
            break
        print(myname.title())
        counter += 1

name = 'jewel'
greet(name)