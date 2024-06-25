'''
SORTING_1_1
#BUBBLESORT
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
def main():
    n=int(input())
    arr=[int(input()) for _ in range(n)]
    bubble_sort(arr)
    print(" ".join(map(str,arr)))
if __name__=="__main__":
    main()

SORTING_1_2
#QUICKSORT
def quicksort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[len(arr)//2]
        left=[x for x in arr if x<pivot]
        middle=[x for x in arr if x==pivot]
        right=[x for x in arr if x>pivot]
        return quicksort(left)+middle+quicksort(right)
n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
sorted_arr=quicksort(arr)
print(" ".join(map(str,sorted_arr)))

SORTING_1_3
#SELECTIONSORT
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
selection_sort(arr)
print(" ".join(map(str,arr)))'''



'''

#sorting_2_1
#sorting arrays
def sort_list(arr):
    arr.sort()
n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
aort_list(arr)
print(arr)

#sorting_2_2
#insertion sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
def main():
    n=int(input())
    arr=list(map(int,input().split()))
    insertion_sort(arr)
    print(" ".join(map(str,arr)))
if __name__=="__main__":
    main()

#sorting_2_3
#bubble sort_1
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
def main():
    n=int(input())
    arr=list(map(int,input().split()))
    bubble_sort(arr)
    print(*arr)
if __name__ == "__main__":
    main()

def shell_sort(arr):
    n=len(arr)
    gap=n//2
    while gap>0:
        for i in range(gap,n):
            temp=arr[i]
            j=i
            while j>=gap and arr[j-gap]>temp:
                arr[j]=arr[j-gap]
                j-=gap
            arr[j]=temp
        gap//=2
def main():
    n=int(input())
    arr=[]
    for _ in range(n):
        arr.append(int(input()))
    shell_sort(arr)
    print(" ".join(map(str,arr)))
if __name__ =="__main__":
    main()'''

'''
#searching_1_1
l=list(map(int,input().split()))
def isin(l):
    s=set()
    for i in l:
        if i*2 in s or (i%2==0 and i//2 in s):
            return True
        s.add(i)
    return False
h=isin(l)
if h==-1:
    print("True")
else:
    print("False")


#searching_1_2
l=list(map(int,input().split()))
xyz=list(map(int,input().split()))
le=xyz[0]-1
ri=xyz[1]
ele=xyz[2]
k=[]
for i in range(le,ri):
    k.append(l[i])
print(k.count(ele))'''

'''
#linked lists_1_1
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked:
    def __init__(self):
        self.head=None
        
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node
    def traversal(self,n):
        curr=self.head
        count=1
        if n%2==0:
            m=(n/2)+1
        else:
            m=n//2+1
        while curr is not None:
            if count==m:
                print(curr.data)
                break
            curr=curr.next
            count+=1
ll=Linked()
n=int(input())
for i in range(n):
    d=int(input())
    ll.add_end(d)
ll.traversal(n)

#functions_18_1
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))
def dinf_minimum_x(n):
    for multiple in range(2*n,101*n,n):
        if sum_of_digits(multiple)==n:
            return multiple
    return -1
n=int(input())
result=find_minimum_x(n)
print(result)



#functions_3_1
def unique_list(numbers):
    unique=[]
    for item in numbers:
        if item not in unique:
            unique.append(item)
    return unique
N=int(input())
numbers=[]
for _ in range(N):
    numbers.append(int(input()))
result=unique_list(numbers)
print(result,end='')


#functions_3_2
import math
def volume(length,breadth,height):
    return length*breadth*height
def surface_area(length,breadth,height):
    return 2*(length*breadth+breadth*height+height*length)
def space_diagonal(length,breadth,height):
    return math.sqrt(lrngth**2+breadth**2+height**2)
length=int(input())
breadth=int(input())
height=int(input())
vol=volume(length,breadth,height)
area=surface_area(length,breadth,height)
diagonal=space_diagonal(length,breadth,height)
print(area)
print(vol)
print("{:.2f}".format(diagonal))


#functions_3_3
def countSetBits(n):
    count=0
    while (n):
        count+=n&1
        n>>=1
    return count
i=int(input())
print(countSetBits(i))

#functions_4_2
def evaluate_polynomial(poly,x):
    result=0
    n=len(poly)
    for i in ramge(n):
        result+=poly[i]*(x**(n-i-1))
    return result
poly=list(map(int,input().split()))
x=int(input())
print(evaluate_polynomial(poly,x))

#functions_4_3
def calculate_exponent(base,exponent):
    if exponent==0:
        return 1
    result=1
    while exponent>0:
        if exponent%2==1:
            result*=base
        base*=base
        exponent//=2
    return float(result)
if __name__=="__main__":
    x,n=map(int,input().split())
    result=calculate_exponent(x,n)
    print(result)


#dictionaries_8_1
from collections import defaultdict
def group_anagrams(arr):
    anagrams=defaultdict(list)
    for word in arr:
        sorted_word=' '.join(sorted(word))
        anagrams[sorted_word].append(word)
    for group in anagrams.values():
        print(' '.join(group),end=' ')
n=int(input())
arr=input().split()
group_anagrams(arr)

#dictionaries_8_2
def remove_substings(dictionary,substrings):
    result={}
    for key, value in dictionsry.items():
        if not any(sub in value for sub in substrings):
            result[key]=value
    return result
n=int(input())
dictionary={}
for _ in range(n):
    key=input()
    value=input()
    dictionary[key]=value
substrings=input().split()
updated_dict=remove_substrings(dictionary,substrings)
output={key:value.split() for key, value, in updated_dict.items()}
print(output)

#dictionaries_8_3
n=int(input())
marks_dict={}
for _ in range(n):
    name=input()
    marks=list(map(int,input().split()))
    marks_dict[name]=marks
sorted_keys=sorted(marks_dict.keys())
sorted_values={key:sorted(marks_dict[key]) for key in sorted_keys}
print(sorted_values)

#dictionaries_9_1
n=int(input())
players={}
for _ in range(n):
    name=input()
    runs=list(map(int,input().split()))
    total_runs=sum(runs)
    playesr[name]=total_runs
sorted_players=dict(sorted(players.items(),key=lambda x: x[1]))
print(sorted_players)

#dictionaries
n=int(input())
my_dict={}
for _ in range(n):
    key,value=input().split()
    my_dict[key]=value
revesed_dict={key:my_dict[key] for key in reversed(my_dict)}
print(reversed_dict)

#dictionaries_9_3
n=int(input())
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
result_dict=dict(zip(list1,list2))
print(result_dict)

#basics_1_1
n=int(input())
if n<=0:
    print("salary should be a positive integer.")
else:
    da=0.4*n
    hra=0.2*n
    gross_salary=n+da+hra
    print("{:.2f}".format(gross_salary))
    
#basics_1_2
distance_km=float(input())
if distance_km<0:
    print("Distance should be a positive number.")
else:
    distance_m=distance_km*1000
    distance_cm=distance_km*100000
    distance_ft=distance_km*3280.8
    distance_in=distance_km*39369.6
    print(distance_m)
    print(distance_cm)
    print("{:.1f}".format(distance_ft))
    print("{:.1f}".format(distance_in))

    

#basics_1_3
s1=float(input())
s2=float(input())
s3=float(input())
s4=float(input())
s5=float(input())
if any(marks<=0 or marks>100 for marks in [s1,s2,s3,s4,s5]):
    print("Marks should be between 1 and 100.")
else:
    aggregate_marks=s1+s2+s3+s4+s5
    total_max_marks=500
    percentage_marks=(aggregate_marks/total_max_marks)*100
    print("{:.0f}".format(aggregate_marks))
    print("{:.1f}".format(percentage_marks))
    
    
#basics_2_1
def main():
    num=int(input())
    e=num%10
    d=(num//10)%10
    c=(num//100)%10
    b=(num//1000)%10
    a=(num//10000)
    print(a+b+c+d+e)
if __name__=="__main__":
    main()
    
#basics_2_2
n=int(input())
rev=0
while(n>0):
    a=n%10
    rev=rev*10+a
    n=n//10
print(rev)

#basics_2_3
import math
def calculate_area_of_triangle(a,b,c):
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area
def main():
    a=int(input())
    b=int(input())
    c=int(input())
    if a<=0 or b<=0 or c<=0:
        print()
        return
    if not (a+b>c and a+c>b and b+c>a):
        print()
        return
    area=calculate_area_of_triangle(a,b,c)
    print(round(area))
if __name__=="__main__":
    main()
    
#basics_3_1  
days=int(input())
if days>0:
    years=days//365
    remaining_days=days%365
    months=remaining_days//30
    remaining_days=remaining_days%30
print(f"{remaining_days}/{months}/{years}")

#basics_3_2
p=int(input())
r=float(input())
t=float(input())
simple_interest=()p*r*t /100
print(simple_interest)

#basics_3_3
num1 = int(input())
num2 = int(input())
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print(num1,end=" ")
print(num2)

#basics_4_1
notes=[100,50,20,10,5,2,1]
amount=int(input())
if amount>0:
    note_count={}
    for note in notes:
        if note==2:
            note_count[note]=0
        else:
            count=amount//note
            note_count[note]=count
            amount-=count*note
    for note in notes:
        print(f"{note}-{note_count[note]}")
        
#basics_4_2
wi1=int(input())
ni1=int(input())
wi2=int(input())
ni2=int(input())
avg=((wi1*ni1)+(wi2*ni2))/(ni1+ni2)
print("{:.0f}".format(int(avg)))

#basics_4_3
C=int(input())
if C>0:
    F=(C*1.8)+32
print(F,"F",end=" ")

#basics_4_4
d=int(input())
print("%o"%d)'''
   
   
   
   
   
   
   
   
   