import pdb

def bubble_sort(l):
    for left in range(len(l)-1,0,-1):
        for i in range(left):
            if l[i] > l[i+1]:
                l[i],l[i+1]=l[i+1],l[i]
                
l = [1,3,2,3]
pdb.set_trace()
bubble_sort(l)
print(l)