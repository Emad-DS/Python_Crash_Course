# numbers = [print(number) for number in range(1, 1_000_001)]
# this is the more succinct way to do what lines 3 through 5 do.
numbers = range(1, 1_000_001)
for number in numbers:
    print(number)