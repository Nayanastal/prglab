list=input("enter a list")
List=[]
for n in list:
    List.append(int(n))
print("The list is \n",List)
print("minimum value from the list",min(List))
print("maximum value from the list",max(List))
print("length of the list",len(List))
print("sum of the list",sum(List))
sort=sorted(List)
print("sort the list",sort)
sort.reverse()
print("reverse of the list",sort)
