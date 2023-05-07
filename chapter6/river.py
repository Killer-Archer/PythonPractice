rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China',
    'Mississippi': 'United States',
    'Danube': 'Germany',
    'Volga': 'Russia',
    'Ganges': 'India',
    'Mekong': 'Vietnam'
}

for river in sorted(rivers.keys()):
	print(f"The {river.title()} runs through {rivers[river]}")
	print(river)
	print(rivers[river])