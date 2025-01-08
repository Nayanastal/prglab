def count_vowels(string):
   
    vowels = "aeiouAEIOU"
    count = 0
    
   
    for char in string:
        if char in vowels:
            count += 1
            
    return count

def replace_vowels_with_hash(string):
   
    vowels = "aeiouAEIOU"
    
   
    result = ''.join('#' if char in vowels else char for char in string)
    
    return result


input_string = input("Enter a string: ")


vowel_count = count_vowels(input_string)
print(f"Number of vowels in the string: {vowel_count}")


modified_string = replace_vowels_with_hash(input_string)
print(f"String after replacing vowels with '#': {modified_string}")
