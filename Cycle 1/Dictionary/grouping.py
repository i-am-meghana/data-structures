def group_by_length(words):
    length_dict = {}
    for word in words:
        length = len(word)
        length_dict[length] = length_dict.get(length, []) + [word]
    return length_dict

# Example
print(group_by_length(["cat", "dog", "elephant", "ant"]))
# Output: {3: ['cat', 'dog', 'ant'], 8: ['elephant']}