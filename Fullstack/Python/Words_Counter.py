# A python program that counts and returns the number of words in a given text.

given_text = "I'm now a Zuri Student, this is my first Python Program as a full-stack Developer"
# given text

print("The given text is : " + given_text)
# using split() function

res = len(given_text.split())

# total no of words
print("The number of words in the given text are : " + str(res))
