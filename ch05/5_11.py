numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number not in [1,2,3]:
        print(f"{number}th")
    elif number==1:
        print(f"{number}st")
    elif number==2:
        print(f"{number}nd")
    else:
        print(f"{number}rd")