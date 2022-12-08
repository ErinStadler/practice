# Write a function that takes in a list of words. Return a list of words that start with a vowel.

# Vowels are aeiou. You don't have to worry about capital letters (although, it makes for a great bonus challenge).

# For example:

def filter_words_starting_with_vowels(words):
    vowels = {"a": True, "e": True, "i": True, "o": True, "u": True, "y": True}
    
    words_starting_with_vowels = []

    for word in words:
        first_letter = word[0].lower()

        if first_letter in vowels:
            words_starting_with_vowels.append(word)

    return words_starting_with_vowels

    
print(filter_words_starting_with_vowels(["elephant", "hello", "octopus"]))
