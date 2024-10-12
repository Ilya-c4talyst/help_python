x, y = 0, 0

while True:

    way_value = input().split()

    if len(way_value) < 2:
        break

    way = way_value[0]
    value = int(way_value[1])

    if way == "N":
        y += value
    elif way == "S":
        y -= value
    elif way == "E":
        x += value
    elif way == "W":
        x -= value

print(x, y)
