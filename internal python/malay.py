class MenuDrivenProgram:
    
    # Method to find the occurrence of each word in a sentence
    def occurrence(self, sentence):
        words = sentence.split()
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        return word_count
    
    # Method to find the frequency of each character in a word
    def frequency(self, word):
        char_count = {}
        for char in word:
            char_count[char] = char_count.get(char, 0) + 1
        return char_count
    
    # Method to find the factors of a given number
    def factors(self, number):
        factor_list = []
        for i in range(1, number + 1):
            if number % i == 0:
                factor_list.append(i)
        return factor_list

# Function to display the menu
def display_menu():
    print("\n1. Occurrence of word")
    print("2. Character frequency")
    print("3. Factors")
    print("4. Exit")

# Main program
def main():
    obj = MenuDrivenProgram()  # Create object of the class
    while True:
        display_menu()  # Display the menu
        choice = int(input("Please Enter a choice from the menu: "))
        
        if choice == 1:
            # Occurrence of each word in a sentence
            sentence = input("Enter a sentence: ")
            word_count = obj.occurrence(sentence)
            print("Occurrence of each word:")
            for word, count in word_count.items():
                print(f"{word}: {count}")
        
        elif choice == 2:
            # Character frequency in a word
            word = input("Enter a word: ")
            char_count = obj.frequency(word)
            print("Character Frequency:")
            for char, count in char_count.items():
                print(f"{char}: {count}")
        
        elif choice == 3:
            # Display the factors of a number
            number = int(input("Enter a number: "))
            factors = obj.factors(number)
            print(f"Factors of {number}:")
            print(factors)
        
        elif choice == 4:
            # Exit the program
            print("Exiting the program...")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

# Run the main function
if __name__ == "__main__":
    main()
