string=input("Enter your word: ")
char=input("Enter your character: ")
i=0
count=0
while i<len(string):
    if string[i]==char:
        count+=1
    i+=1
print("The total nimber of times",char,"has occured= ",count)