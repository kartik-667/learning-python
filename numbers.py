import random
def log(ans):
    print(ans)

a=123
x=1
y=2
z=3

# for sets and maps , use {}
#  for set, insert single val
#  for map, insert a key value pair

def find_set_bits(n):

    num=n;
    cnt=0;

    while(num>0):
        if(num & 1):
            cnt+=1
        num>>=1
    
    print(cnt)

find_set_bits(8)

def test1():
    l1=[1,2,3,4,5,6]
    val=random.choice(l1)
    if(val): print(val)


test1()


# for i in str(a):
    # print(i,end=" ")


