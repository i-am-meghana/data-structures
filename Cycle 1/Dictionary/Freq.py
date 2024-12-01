#find the frequency of characters
def freq(s):
    dict_freq = {}
    for char in s:
        if char in dict_freq:
            dict_freq[char] += 1
        else:
            dict_freq[char] = 1
    return dict_freq



print(freq("apple"))

#edge cases?

#given a sentence find the frequence of its words
def word_frequency(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

print(word_frequency("the the The is tHe"))


#given a list of integers find the most frequent element
#[1,2,3,4,4,4,5,6,2,2,7]
def freq_ele(num):
    dict = {}
    for n in num:
        if n in dict:
            dict[n] += 1
        else:
            dict[n] = 1
    #we can sort the values or we can check for the highest value in dict
    #iteration through dictionary in Python is iteration through it's keys?