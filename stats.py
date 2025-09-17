from collections import Counter

def count_words(text): 
    words = text.split()
    num_words = len(words)
    return num_words

def count_characters(text):
    dictionary = {}
    counts = Counter(text.lower())
    for k,v in counts.items():
        if k.isalpha():
            dictionary[k] = v
    return dictionary

def set_response(dictionary):

    char_list= []

    for ch, count in dictionary.items():
        char_list.append({"char": ch, "num": count})
    
    def sort_on(items):
        return items["num"]

    char_list.sort(reverse=True, key=sort_on)
    
    return char_list

""" def count_characters(text):
    dictionary = {}
    for char in text.lower():
        if char.isalpha():  # only letters
            if char in dictionary:
                dictionary[char] += 1  # increment
            else:
                dictionary[char] = 1   # first occurrence
    return dictionary """

    
