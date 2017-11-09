numbers = [10, 2, 1, 4, 20]
output = []

while numbers:
    smallest = min(numbers)
    index = numbers.index(smallest)
    output.append(numbers.pop(index))

print(output)
