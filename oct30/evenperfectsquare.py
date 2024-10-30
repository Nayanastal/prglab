First=int(input("Enter lower range: "))
Last=int(input("Enter upper range: "))
a=[]
a=[x for x in range(First,Last+1) if (int(x**0.5))**2==x]
print(a)
print("even perfect square are: ")
b=[]
for a in range(First,Last+1):
     i=int(a**0.5)
     if i*i==a and a %2==0:
         b.append(a)
         print (b)
