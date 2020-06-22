# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 11:41:18 2020

@author: Vedanti
"""

print("enter a word")
ip = input()
#print(ip)
#print(ip[0],"",ip[1],"",ip[2])
op=""
for i in range(len(ip)):
    op=op+"-"
print("you have six chances to guess the word")
for i in range(0,6):
    print("enter",i, "guess")
    guess = input()
    for j in range(len(ip)):
        count=0
        if guess == ip[j]:
            op=op[:j]+guess+op[j+1:]
        else:
            count=count+1
    if(count!=0):
        print(guess,"is not in given word")
    print("till now output is ",op)
    if(ip==op):
        break;
if(ip==op):
    print("YOU WON!!")
else:
    print("TRY WITH ANOTHER WORD")
