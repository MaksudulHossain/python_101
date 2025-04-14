scientists = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        'discovery': 'Theory of Relativity',
        'nobel_year': 1921,
        'important_fact': 'He won the Nobel Prize for the photoelectric effect, not relativity.',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        'discovery': 'Radioactivity and elements polonium & radium',
        'nobel_year': [1903, 1911],
        'important_fact': 'She was the first person to win Nobel Prizes in two different sciences.',
    },
}

for name, info in scientists.items():
    fullname = f"{info['first']} {info['last']}"
    print(f"fullanme: {fullname}")
    for k, v in info.items():
        print(f"{k}: {v}")
    print()