def read_number():
   
    try:
        num = int(input("Enter a number: "))
        return num
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return None

def is_armstrong(num):
    
    if num is None:
        return False
    
   
    digits = str(num)
    num_digits = len(digits)
    
   
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    
    
    return sum_of_powers == num


number = read_number()

if number is not None:
    if is_armstrong(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")
