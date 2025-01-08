class StringOperations:
    def __init__(self, string):
        self.string = string

    def is_palindrome(self):
        
        cleaned_string = self.string.replace(" ", "").lower()
        return cleaned_string == cleaned_string[::-1]

    def count_vowels(self):
        vowels = "aeiouAEIOU"
        count = 0
        for char in self.string:
            if char in vowels:
                count += 1
        return count

    def reverse_string(self):
        return self.string[::-1]


def menu():
    while True:
        
        print("\nMenu:")
        print("a. Check Palindrome")
        print("b. Count Vowels")
        print("c. Reverse String")
        print("d. Exit")

        
        choice = input("Enter your choice: ").strip().lower()

        if choice == 'd':
            print("Exiting the program.")
            break

        if choice not in ['a', 'b', 'c']:
            print("Invalid choice! Please choose a valid option.")
            continue

       
        input_string = input("Enter a string: ").strip()

        
        string_operations = StringOperations(input_string)

       
        if choice == 'a':
            if string_operations.is_palindrome():
                print("The string is a palindrome.")
            else:
                print("The string is not a palindrome.")
        elif choice == 'b':
            print(f"The number of vowels in the string is: {string_operations.count_vowels()}")
        elif choice == 'c':
            print(f"The reversed string is: {string_operations.reverse_string()}")


if __name__ == "__main__":
    menu()
