


"""
Task3
unique country stamps
"""



n = int(input())
stamps = set()

for i in range(0,n):
    countries = input().strip()
    stamps.add(countries)
    
print(len(stamps))