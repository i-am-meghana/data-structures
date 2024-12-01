def categorize_numbers(nums):
    categories = {}
    for num in nums:
        category = "even" if num % 2 == 0 else "odd"
        categories[category] = categories.get(category, []) + [num]
    return categories

# Example
print(categorize_numbers([1, 2, 3, 4, 5, 6]))
# Output: {'odd': [1, 3, 5], 'even': [2, 4, 