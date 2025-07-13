favorite_number = {
    'sunny':1,
    'abul':2,
    'jewel':3,
    'shimul':4,
    'mishu':5
}

for k, v in favorite_number.items():
    print(f"{k}'s favorite number = {v}")

poll = {}
friends = ['sunny','abul','jewel','shimul','mishu']
for friend in friends:
    poll[friend] = int(input(f"{friend}, What is your favorite number? "))

for k,v in poll.items():
    print(f"{k}'s favorite number is {v}")
