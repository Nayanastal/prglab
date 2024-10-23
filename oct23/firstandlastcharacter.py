string=input("Enter text:")
if len(string)>1:
    string=string[-1]+string[1:-1]+string[0]
print("list after swapping first to last and last to first element",string)
 
