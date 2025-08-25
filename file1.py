
import math
import random

import sys

print("the ref count is",sys.getrefcount("kartik"))

randval=random.random() * 10
randval=math.floor(randval)
print(randval)
# print(math.factorial(12))


def func1():
    print("this is fnc 1")


def check_sorted(arr):

    if(len(arr)<=1): return True

    for i in range(1,len(arr)):
        if(arr[i-1] > arr[i]):
            return False

    return True

def binary_search(arr,val):
    if(check_sorted(arr)==False): # in case not sorted, so sort it
         arr.sort()
        
    left=0
    right=len(arr)-1

    while(left<=right):
        mid=(left + right) //2
        if(val==arr[mid]):
            print("val found")
            return
        elif(val < arr[mid]):
            right=mid-1
        else:
            left=mid+1
    
    print("val not found")

def dfs_graph(node,vis,adj):

    vis.append(node)
    print(node)

    for adjn in adj[node]:
        if adjn not in vis:
            dfs_graph(adjn,vis,adj)


    # here it will backtack

def graph_main():
    adj=[[1,2],[4,5],[5,6]]
    vis=[]
    
    
    dfs_graph(0,vis,adj)

    print("function completed here")
    

name="kartikkkaskdkasdkakskdaksksd"
count=0

for i in name:
    if(i=='k'): count+=1


# print("enter your name")
# # name2=input()

# print("the inputed name is",name2)
# print(count,end=" ")

# list1=[]
# list1.append(1)

# print(list1)
