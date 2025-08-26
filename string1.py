a="kartik k k k k k k k kk verma is gonna boom bro"
list1=a.split(' ') # eg split by space 
print(list1)

hmap={}

for char in a:
    if(char==' ' or char==''): continue
    if(char in hmap):
        hmap[char]+=1
    else:
        hmap[char]=1

print(hmap)

print(f'the fstring is {hmap}') # this is how we use placeholder
