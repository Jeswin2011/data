list1=["lol","hi","sos", "good"]

def match(words):
    count=0
    list2=[]
    for w in words:
        if w[0]==w[-1]:
            count+=1
            list2.append(w)
    return list2
newlist=match(list1)

print(newlist)
        
