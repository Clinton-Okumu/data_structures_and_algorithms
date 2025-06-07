# A list is mutable, ordered collection of items. It can hold elements of any data type.

my_list = [1, 2, 3, 4, 5, "hello", True]
nums = [1, 2, 3, 4, 5]

# creating and indexing
nums[0]
nums[-1]
nums[2:4]

# iterating

for i in nums:
    print(i)

# methods
nums.append(6)
nums.extend([7, 15])
print(f"Extended 7 and 15: {nums}")
nums.insert(2, 12)
print(f"Inserted 12: {nums}")
nums.remove(12)
print(f"Removed 12: {nums}")
nums.pop(1)
print(f"Popped 1: {nums}")
nums.index(4)
print(f"Index of 4: {nums.index(4)}")
nums.sort()
print(f"Sorted: {nums}")
nums.clear()
print(f"Cleared: {nums}")
