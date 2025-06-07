# A `tuple` is an **immutable**, ordered collection of items. Once created, its contents **cannot be changed** (no adding, removing, or modifying).

my_tuple = (1, 2, 3)


empty = ()
singleton = (1,)  # Must include the comma
mixed = (1, "hello", True)
nested = ((1, 2), (3, 4))

# indexing and slicing

t = (10, 20, 30)
t[0]  # 10
t[-1]  # 30
t[1:3]  # (20, 30)

for i in t:
    print(i)
