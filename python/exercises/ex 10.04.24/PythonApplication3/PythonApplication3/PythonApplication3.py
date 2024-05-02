 

# def hhh(a):
#  for r in range(len (a)):
#      for c in range(len(a[0])):
#         print(a[r][c],end="  ")
#      print()
a=[
   [1,2,3,4,5],
   [3,4,5,9,8],
   [7,8,3,2,5],
   [6,1,4,3,2]
   ]
for c in range(len(a[0])):
   temp= a[0][c]
   for r in range(len(a)-1):
      a[r][c]=a[r+1][c]
   a[r+1][c]=temp
   
for r in range(len (a)):
    for c in range(len(a[0])):
       print(a[r][c],end="  ")
    print()
    #print(hhh(a))