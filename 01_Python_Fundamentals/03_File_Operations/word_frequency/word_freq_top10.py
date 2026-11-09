import jieba
with open("二十大.txt", "r", encoding="utf-8") as f:
    txt = f.read()
ls=jieba.cut(txt)
counts={}
for word in ls:
    counts[word]=counts.get(word,0)+1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))