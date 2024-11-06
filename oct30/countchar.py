String=input("Enter the string : ")
for char in set(String):
    count=0;
    for c in String:
        if c==char:
            count+=1
    print(char, ":" ,count)
