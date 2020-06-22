print("enter a word")
ip = input()
op=ip
for i in range(len(op)):
    if(ip[i].isalpha()):
        op=op[:i]+"-"+op[i+1:]
print(op)
print("you have six chances to guess the word")
for i in range(0,6):
    print("enter",i, "guess")
    guess = input()
    if guess in ip:
        for j in range(len(ip)):
            if guess == ip[j]:
                op=op[:j]+guess+op[j+1:]
        print("till now output is ",op)
        if(ip==op):
            break;
    else:
        print(guess,"is not in given word")

    
if(ip==op):
    print("YOU WON!!")
else:
    print("TRY WITH ANOTHER WORD")
