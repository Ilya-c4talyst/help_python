number = int(input())

result_fact = 1
counter = 1

while counter <= number:

    result_fact *= counter
    counter += 1

print(result_fact)
