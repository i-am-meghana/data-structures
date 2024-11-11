def freq(s):
    dict_freq = {}
    for char in s:
        if char in dict_freq:
            dict_freq[char] += 1
        else:
            dict_freq[char] = 1
    return dict_freq

print(freq("apple"))