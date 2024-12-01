def non_repeat(s):
    dict_freq = {}
    for char in s:
        if char in dict_freq:
            dict_freq[char] += 1
        else:
            dict_freq[char] = 1
    
    for char in s:
        if dict_freq[char] == 1:
            return char
print(non_repeat("aapple"))



#also return stts when theres 2 for loops - reach the first return and stops func exe. no code below is run.
#why is it printing e in the below logic?
#if dict_freq[char] == 1:
#  temp=char
#return temp
#this runs the loop for e as well. it finds l stores it in temp. then goes to next char is s. sees e is 1 goes into if loop and updates temp as e and returns e

    