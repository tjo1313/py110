# Modify the word_sizes function from the previous exercise to exclude 
# non-letters when determining word size. For instance, the word size 
# of "it's" is 3, not 4.

def word_sizes(words):
    words_list = words.split()
    
    counts = {}
    for word in words_list:
        clean_word = exclude_nonletters(word)
        word_size = len(clean_word)
        if word_size not in counts:
            counts[word_size] = 1
        else:
            counts[word_size] += 1
    
    return counts

def exclude_nonletters(word):
    new_word = ''
    for char in word:
        if char.isalnum():
            new_word += char
    
    return new_word



# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})