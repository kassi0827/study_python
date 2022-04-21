seat = []

min = 0
max = 5

print(min <= len(seat) <= max)

seat.append('p')
seat.append('p')
seat.append('p')
seat.append('p')
seat.append('p')

print(min <= len(seat) <= max)

seat.append('p')

print(min <= len(seat) <= max)

seat.pop(0)

print(min <= len(seat) <= max)
print(len(seat))
seat.pop(0)
print(len(seat))
