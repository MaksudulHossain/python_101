favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

people = ['jen','sarah','rocky','jason','russel']

for person in people:
    if person in favorite_languages.keys():
        print(f"Thanks for participating in poll, {person}")
    else:
        print(f"{person}, can you please participate in the poll?")