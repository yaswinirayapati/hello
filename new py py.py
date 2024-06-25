'''def multiply(a,b):
    return a*b
result=multiply(5,0) or multiply(3,4)
print(result)

x=[1,2,3]
y=x*2
y[0]=0
print(y)

def func(x):
    return x*2
result=func(2)
result=func(result)
result=func(result)
print(result)

def baz(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i]==lst[j]:
                return True
    return False
print(baz[1,2,3,4,5,5])

*_,='Python'
print(_)

a=3
b=1
for c in range(2,6):
    a=a-c
    a=a*c
print(a+b)

a=(10,20,30)
b=(40,)
print(a+b)

def solve(a):
    return a[-1]
a=[1,2,3,4]
print(solve(a))**2

print(isinstance('False',bool))

x=0.1
y=0.2
print((x+y)==True)

st1="python learning"
st2=st1[:5]*2+st1[:4]
st3=st2[:5//2]*3
print(st3)

a=[1,2,3,5]
if a.sort()==sorted(a):
    print("cow")
else:
    print("dog")

t_=(5,0)
print(t_*2)

x=["ab","cd"]
for i in x:
    x.append(i.upper())
    print(x)

str='python'
print(str)
x=100
y=str(x)
print(y)'''
