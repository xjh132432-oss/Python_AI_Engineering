import random
ls=[]
def list_():
    ls1=[]
    for j in range(5):
        w = random.randint(0, 9)
        ls1.append(w)
    return ls1
with open("random.csv", "w+", encoding="utf-8")as f:
    for i in range(5):
        re=list_()
        ls.append(re)
        line_str = ",".join(map(str, re))
        f.write(line_str + "\n")
    for line in ls:
        print(line)