glossary = {
    'loop': 'repeating same tasks',
    'variable': 'stores objects',
    'datatype': 'what type of data we are storing',
    'function': 'package codes that are used frequently in the code',
    'list': 'array like data structure, index based accessing',
}

for k, v in glossary.items():
    print(f"{k}:\n\t-{v}")

more_words = ['recursion', 'dictionary','module','method', 'object']
explanation = [
    'function calling itself',
    'hash-map table: key-value pair',
    'python code with functions and variables',
    'function bound to a class',
    'encapsulation of data and method'
]
for idx, word in enumerate(more_words):
    glossary[word] = explanation[idx]

for k, v in glossary.items():
    print(f"{k}:\n\t-{v}")
