# Create a Python program that:
#
# Takes a user-input sentence.
# Analyzes and prints:
# Number of characters
# Number of words
# Number of vowels & consonants
# Whether the sentence starts or ends with a specific word
# The longest word
# The sentence reversed

def count_vowel_consonants(s):
    vowels = "aeiouAEIOU"
    v_count=c_count=0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v_count+=1
            else:
                c_count+=1
    return v_count,c_count

def longest_word(sentence):
    words = sentence.split()
    longest=""
    for word in words:
        if len(word) > len(longest):
            longest=word
    return longest

# main Program
sentence = input("Enter a sentence:").strip()
char_count = len(sentence)
word_count = len(sentence.split()) #count of word by converting string to char array
vowels,consonants = count_vowel_consonants(sentence)
longest = longest_word(sentence)
starts = sentence.startswith("Python")
ends = sentence.endswith("!")

print(f"\nCharacter count: {char_count}")
print(f"Word count: {word_count}")
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Starts with 'Python': {starts}")
print(f"Ends with '!': {ends}")
print(f"Longest word: {longest}")
print(f"Reversed sentence: {sentence[::-1]}")