def find_longest_word_length(words):
    # Find the longest word in the list
    longest_word = max(words, key=len)
    # Return the length of the longest word
    return len(longest_word)

# Accept list of words from the user
words = input("Enter a list of words separated by spaces: ").split()

# Find and print the length of the longest word
longest_length = find_longest_word_length(words)
print("The length of the longest word is:", longest_length)
