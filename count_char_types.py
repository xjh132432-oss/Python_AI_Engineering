s=input("please enter")
eng=0
digit=0
space=0
oth=0
for i in range(0,len(s)):
    #digit
    if s[i].isdigit():
        digit+=1
    #eng
    elif ('a'<=s[i]<='z') or ('A'<=s[i]<='Z'):
        eng+=1
    #space
    elif s[i]==" ":
        space+=1
    #oth
    else :
        oth+=1
print("数字个数:{}英文个数:{}空格个数:{}其它字符个数:{}".format(digit,eng,space,oth))