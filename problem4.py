list=[1,2,3,4,4,5,67,73,87,95,100]
print(list)
b=int(input("enter the element to be searched"))
list1=[]
for i in range(0,len(list)):
	if list[i]==b:
		list1.append(i)
print(list1)
