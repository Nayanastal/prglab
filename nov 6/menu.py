list1=[]

n=int(input("enter the range of number:"))
for i in range(1,n+1):
    a=int(input("enter values:"))
    list1.append(a)

print(list1)
while True:
    print("\n select your choice:")
    print("1.find greatest and lowest number")
    print("2.sort acending order")
    print("3.create new list of even numbers")
    print("4.exit")
    choice = int(input("select your choice:"))
    if choice == 1:
        print("the greatest value is",max(list1))
        print("the lowest value is",min(list1))
    elif choice ==2:
        print("ascending order list",sorted(list1))
    elif choice ==3:
        newlist=[]
        for i in list1:
            if i%2==0:
                newlist.append(i)
        print("even numbers new list",newlist)
    else:
        break
                
        
        
    
    
