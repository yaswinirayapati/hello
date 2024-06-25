def linearSearch(l,s):
    loc=-1
    for i in l:
        if i==s:
            loc=l.index(i)
            break
    
    return loc
if __name__="__main__":
    n=int(input("input the list size"))
    lst=list(map(int(input().split())))
#lst=[]
#for i in range(n):
#    lst.append(int(input("enter an element"))):

se=int(input('enter the search element'))
loc=linearSearch(lst,se)
if loc>=0:
    print('element is found at %d position'%(loc))
else:
    print('element is not found')
               