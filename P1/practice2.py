#随机输出一句话
__author__ = 'hiCyoung'
import random

GC=["the","a"]
ZT=["cat","dog","man","woman"]
DC=["sang","ran","jumped"]
ZY=["loudly","quietly","well","badly"]
#以下拼接字符串效率低
# word1=''.join(random.choice(GC))+"".join(" "+random.choice(ZT))+"".join(" "+random.choice(DC))+"".join(" "+random.choice(ZY))
# word2=''.join(random.choice(GC))+"".join(" "+random.choice(ZT))+"".join(" "+random.choice(DC))
wordsList=[]
wordsList.append(random.choice(GC))
wordsList.append(random.choice(ZT))
wordsList.append(random.choice(DC))

wordType = random.randint(1,3)
if wordType==1:
    word = "  ".join(wordsList)
else:
    wordsList.append(random.choice(ZY))
    word = " ".join(wordsList)
print(word)
