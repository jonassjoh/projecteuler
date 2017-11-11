def get_numbers():
    numbers = []
    with open('numbers.in') as f:
        for line in f:
            numbers.append(int(line))
    return numbers

numbers = get_numbers();

print(str(sum(numbers))[:10]);
