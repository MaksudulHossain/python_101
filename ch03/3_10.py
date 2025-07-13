mountains = ["Everest", "K2", "Kangchenjunga", "Lhotse", "Makalu"]
everset_index = mountains.index("Everest")
mountains.append('Kilimanjaro')
mountains.insert(1,'Denali')
mountains.remove("Everest")
first_mountain = mountains.pop(0)
last_mountain = mountains.pop()
print("just reversing list, not alphabetical")
print(reversed(mountains))
print("sorted not in place")
print(sorted(mountains))
mountains.sort(reverse=True)
print(mountains)

del mountains[3]