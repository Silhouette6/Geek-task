#写完了才发现原来师兄有模板www
#思路可能有点奇怪，望见谅，但终究是把功能实现出来了
word={}
dic={}
objlist=[]
n=-2
n1=0
out=''

def arrange(dic):
    dic1=dic
    dic2={}
    chg=1
    while True:
        chg=0
        First=1
        n=0
        for i in dic1:
            n+=1
            if First:
                key=i
                mv=dic[i]
                First=0
            if dic[i]<mv and First==0:
                key=i
                mv=dic[i]
        dic2[key]=mv
        dic1.pop(key)
        if n==1:
            break
    return dic2
def Creat(a,b,dic):
    ak=dic[a]
    bk=dic[b]
    Tk=ak+bk
    dic.pop(a)
    dic.pop(b)
    dic[a+','+b]=Tk
    ejz1=a.split(sep=',')
    for e1 in ejz1:
        word[e1]='1'+word[e1]
    ejz0=b.split(sep=',')
    for e0 in ejz0:
        word[e0]='0'+word[e0]

    global glb
    glb=a+','+b
    return 0
def CT(dic):
    nc=0
    for i in dic:
        nc+=1
        if nc==1:
            a=i
        if nc==2:
            b=i
            Creat(a=a,b=b,dic=dic)
            break


#x = input('请输入需要压缩的字符串:')
x = 'aaadsssdffr'
for i in x:
    word[i]=''
    if i in dic:
        dic[i] = int(dic[i]) + 1
    else:
      dic[i] = 1
for obj in dic:
    objlist.append(obj)
for l in dic:
    n+=1

dic2=arrange(dic)

while n1<=n:
    CT(dic2)
    g=glb.split(sep=',')
    dic2=arrange(dic2)
    n1+=1

for mhf in objlist:
    print(mhf,'的哈夫曼二进制编码为',word[mhf])

for w in x:
    out=out+','+word[w]
print('------------------------------------------')
print('\033[1;31m压缩完成！\033[0m')
print(x,'的压缩结果为：',out)