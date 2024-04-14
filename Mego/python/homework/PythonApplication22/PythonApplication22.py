



from pickle import TRUE
import random
import string
from tkinter import CHAR


print("                  Welcome to the game Hangman")

HANGMAN_ASCII_ART=("""

                    Welcome to the game Hangman                                      
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
              
""")
      
MAX_TRIES= (random.randint(5,10))

print("""    x-------x        \n\n""")


print("""    x-------x
    |
    |
    |
    |
    |
""")
print("""     x-------x
    |       |
    |       0
    |
    |
    |
""")
print("""    x-------x
    |       |
    |       0
    |       |
    |
    |

""")
print("""    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
""")
print("""    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
""")
print("""    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |""")



print(HANGMAN_ASCII_ART,MAX_TRIES)


guessing_letter = input("Guess a letter: ")

guessing_letter = guessing_letter.lower()

def is_valid_input(letter_guessed):

  if len(letter_guessed) > 1 and not all(char.isalpha() and char in 'abcdefg\
     hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for char in letter_guessed):
    print("E3")
    return False

  elif len(letter_guessed) > 1:
    print("E1")
    return False

  elif not all(char.isalpha() and char in 'abcdefghijk\
   lmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for char in letter_guessed):
    print("E2")
    return False

  return True

  

print(is_valid_input(guessing_letter))

string_of_his_choice = input(" string of his choice: ")
i = len (string_of_his_choice)


while(i>0):
    print ("_", end= " ")
    i-=1
    





# num=int(input("Enter a number : "))
# max=num
# min=num
# while(num<100 or num>999):
#     if(max<num):
#         max=num
#     if(min>num):
#         min=num
#     num=int(input("Enter a number : "))
# if(max<num):
#     max=num
# if(min>num):
#     min=num

# print(max, min)    





# num=int(input("Enter a number : "))
# max=num
# min=num
# while(num<100 or num>999):
#     if(max<num):
#         max=num
#     if(min>num):
#         min=num
#     num=int(input("Enter a number : "))
# if(max<num):
#     max=num
# if(min>num):
#     min=num

# print(max, min)    




# import random
# letters="abcdefghijklmnopqrstuvwxyz"
# hatspan=["a","b","c","d","e","f","g","h","i","j","k","l","m",
#          "n","o","p","q","r","s","t","u","v","w","x","y","z"]
# swapCount=random.randint(22,66)
# for i in range(swapCount):
#     idx1=random.randint(0,len(letters)-1)
#     idx2=random.randint(0,len(letters)-1)
#     ezer=hatspan[idx1]
#     hatspan[idx1]=hatspan[idx2]
#     hatspan[idx2]=ezer
# print(hatspan)

# text="bokertov"
# newText=""
# for i in range(len(text)):
#     idx= ord(text[i])-ord('a')
#     newText=newText + hatspan[idx]
# print(newText)

'''
['a', 's', 't', 'v', 'd', 'r', 'i', 'x', 'u',
 'k', 'h', 'l', 'w', 'n', 'j', 'f', 'm', 'y',
 'q', 'g', 'p', 'o', 'b', 'z', 'c', 'e']
['s', 'j', 'h', 'd', 'y', 'g', 'j', 'o']
'''
#['n','m','b','t','c','z','q','g','r','j','v','k','o',
# 'y','h','l','p','i','u','f','w','s','d','x','a','e']
print()



# import random
# letters=["a","b","c","d","e","f","g","h","i","j","k","l","m",
#          "n","o","p","q","r","s","t","u","v","w","x","y","z"]
# hatspan=["a","b","c","d","e","f","g","h","i","j","k","l","m",
#          "n","o","p","q","r","s","t","u","v","w","x","y","z"]
# swapCount=random.randint(22,66)
# for i in range(swapCount):
#     idx1=random.randint(0,len(letters)-1)
#     idx2=random.randint(0,len(letters)-1)
#     ezer=hatspan[idx1]
#     hatspan[idx1]=hatspan[idx2]
#     hatspan[idx2]=ezer
# print(hatspan)

# text="bokertov"
# newText=[""]*len(text)
# for i in range(len(text)):
#     idx= ord(text[i])-ord('a')
#     newText[i]=hatspan[idx]
# print(newText)



# '''
# ['a', 's', 't', 'v', 'd', 'r', 'i', 'x', 'u',
#  'k', 'h', 'l', 'w', 'n', 'j', 'f', 'm', 'y',
#  'q', 'g', 'p', 'o', 'b', 'z', 'c', 'e']
# ['s', 'j', 'h', 'd', 'y', 'g', 'j', 'o']
# '''
# #['n','m','b','t','c','z','q','g','r','j','v','k','o',
# # 'y','h','l','p','i','u','f','w','s','d','x','a','e']
# print()

# string_of_his_choice = input(" string of his choice: ")
# half_length = len (string_of_his_choice) // 2

# new_string = string_of_his_choice[:half_length]\
# .lower() + string_of_his_choice[half_length:].upper()

# print(new_string)
