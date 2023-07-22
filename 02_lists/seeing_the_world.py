locations = ['tokio', 'amsterdam', 'milan', 'valencia', 'chicago']
print(locations)
# alphabetical order
print(sorted(locations))
print(locations)
# reverse-alphabetical order
print(sorted(locations, reverse=True))
print(locations)
# reverse chronological order
locations.reverse()
print(locations)
# back to chronological order
locations.reverse()
print(locations)
# alphabetical order permanently
locations.sort()
print(locations)
# reverse-alphabetical order permanently
locations.sort(reverse=True)
print(locations)