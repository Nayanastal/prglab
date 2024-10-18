
list=input("Enter the First name : ")
Name=list.split()
print("list is",Name)
count=0
for name in Name:
    count+=name.lower().count('a')
print("occurence of a is : ",count)
