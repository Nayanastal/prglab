a = []
size = int(input("Enter the size : "));
for i in range(0,size):
    b=int (input("Enter the elements :"));
    if b<=100:
         a.append(b)
    else:
         a.append("over")
print(a)
