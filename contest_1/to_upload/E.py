countries_events = input().split(', ')

countries_high_quality = input().split(', ')

countries_interested = input().split(', ')

result = []

for country in countries_interested:

    if (country in countries_high_quality) and (country not in countries_events):
        result.append(country)

    elif (country not in countries_high_quality) and (country in countries_events):
        result.append(country)


result = sorted(result)
print(', '.join(result))
