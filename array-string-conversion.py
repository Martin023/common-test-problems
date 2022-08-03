# Converting an array to a string
# method 1 using for loop ,method 2 using join method 3 using map method
def smash(words):
    str = ""
    for item in words:
        str += item
        return str


print(smash(["hello", "world"]))
print(smash(["hello", " ", "world"]))
smash(["hello", " ", "world"])

#####################
# Array to String method 2 using join method

# def smash(words):
#     print(" ".join(words)) 

# smash(["hello", "world"])

# #method 3 using map
# def smash(words):
#     return " ".join(map(str, words))





# kata prob
# Sentence Smash
# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

# Example
# ['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

def smash(words):
    return " ".join(words)
