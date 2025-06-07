# A `set` is an **unordered**, **mutable**, collection of **unique** elements. It is similar to a mathematical set.

empty_set = set()

nums = {
    1,
    2,
    3,
    4,
    4,
}

# adding
nums.add(6)
print(nums)

# removing
nums.remove(6)

# iterating
for i in nums:
    print(i)

nums.update([5, 6, 7])
print(nums)

nums.clear()
print(nums)
