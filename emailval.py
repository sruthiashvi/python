import re
list=[]
n=int(input())
for i in range(n):
    email=input()
    match=re.search(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',email)
    if match!=None:
        list.append(email)
list.sort()
print(list)
'''lst=[6,3,4,1,2]
print(len(lst))
for i in range(1,len(lst)):
    for j in range(i):
        if lst[i]<lst[j]:
            tmp=lst[i]
            lst[i]=lst[j]
            lst[j]=tmp'''
