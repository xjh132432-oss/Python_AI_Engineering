import jieba
import wordcloud
with open("二十大.txt","r",encoding="UTF-8")as f:
    ls=jieba.lcut(f.read())
for i in range(len(ls)-1,-1,-1):
    if len(ls[i])<=1:
        del ls[i]
w=wordcloud.WordCloud(\
width=1000,height=1000,\
background_color="white",\
font_path="msyh.ttc"\
  )
txt=" ".join(ls)
w.generate(txt)
w.to_file("wordcloud.png")
