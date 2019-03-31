def Count(start, stop):
    while start <= stop:
        yield start
        start += 1


for i in Count(101, 109):
    print(i)
print()
even = (e for e in range(10) if not e % 2)
odd = (e for e in range(10) if e % 2)
print(sum(even))
print(sum(odd))
