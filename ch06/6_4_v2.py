glossary = {
    'loop': 'repeating same tasks',
    'variable': 'stores objects',
    'datatype': 'what type of data we are storing',
    'function': 'package codes that are used frequently in the code',
    'list': 'array like data structure, index based accessing',
}

for k, v in glossary.items():
    print(f"{k}: {v}")

more_items = [
    ('key', 'the unique index of dict items'),
    ('value', 'values corresponding to dict keys'),
    ('dict', 'hash map datastructuire implementation in python'),
    ('tuple', 'immutable data type, list without super power'),
    ('int', 'primitive datatype to store integer'),
]

for k, v in more_items:
    glossary[k] = v 

# altogether
for k, v in glossary.items():
    print(f"{k}:\n\t{v}")