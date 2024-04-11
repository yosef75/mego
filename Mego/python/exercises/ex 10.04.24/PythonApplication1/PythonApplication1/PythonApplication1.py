a=[
    [3,5,6,6,9],
    [3,5,4,1,2],
    [7,4,5,6,7],
    [1,2,3,4,0],
]
m=0
for r in range(len(a)):
    for c in range(len(a[r])-1):
       if  ((a[r][c])+1)==(a[r][c+1]):
           m+=1    
print(m)
