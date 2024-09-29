# Generators in Python
def my_generator():
    for i in range(23):
        yield i


gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))

print("\nPrinting All Values")
for j in gen:
    print(j)