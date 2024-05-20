# x= int(input("enter num\n"))
# big = 0
# small=0
# small=small+x
# big=big+x
# while(x<100):
    
    
#     x= int(input("enter num\n"))
#     if(big<x):
#         big=0
#         big=big+x
#     if(small>x):
#         small=0
#         small=small+x

# print(big)
# print(small)
   


def aaa(a):
    if len(a)%2==0:   
        return False
    if( a[0]==a[-1]==a[(len(a)//2)]):
        return True
    return False

print(aaa(input("enter string\n")))