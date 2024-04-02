# Given a string of words separated by spaces, write a function that 
# swaps the first and last letters of every word.

# You may assume that every word contains at least one letter, and that 
# the string will always contain at least one word. You may also assume 
#that each string contains nothing but words and spaces, and that there 
# are no leading, trailing, or repeated spaces.

def swap(words):
    words_list = words.split()
    swapped_words_list = []

    for word in words_list:
        updated_word = ''
        index = 0
        while index < len(word):
            if index == 0:
                updated_word += word[-1]
            elif index == (len(word) - 1):
                updated_word += word[0]
            else:
                updated_word += word[index]

            index += 1

        swapped_words_list.append(updated_word)

    return ' '.join(swapped_words_list)
   

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True