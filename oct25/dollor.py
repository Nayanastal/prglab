string=input("Enter a string:")
new_string=string[0]+string[1:].replace(string[0],'$')
print("new string:",new_string)
