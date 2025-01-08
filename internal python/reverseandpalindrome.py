def reverse_string(s):
    
    return s[::-1]

def is_palindrome(s):
    
    return s == reverse_string(s)


input_string = input("Enter a string: ")


reversed_string = reverse_string(input_string)


if is_palindrome(input_string):
    print(f"The string '{input_string}' is a palindrome.")
else:
    print(f"The string '{input_string}' is not a palindrome.")
