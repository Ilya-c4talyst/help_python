a, b = map(int, input().split())

result = []

for i in range(a, b + 1):

    if i % 3 == 0 and i % 5 == 0:
        result.append('fizzbuzz')
    
    elif i % 5 == 0:
        result.append('buzz')

    elif i % 3 == 0:
        result.append('fizz')

    else:
        result.append(str(i))

print(' '.join(result))