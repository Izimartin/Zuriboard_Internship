# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if(sorted(word) == sorted(anagram)):
        print("They are anagrams")
        return True
    else:
        print("Not an anagram")
        return False


find_anagram("hello", "check")
find_anagram("below", "elbow")
