l={}
for i in range(int(input("Enter the number of words:"))):
    x=input("Enter the word:")
    if x not in l:
        l[x]=1
    else:
        l[x]=l[x]+1
print(len(l))
for i in l:
    print(l[i],end=" ")
