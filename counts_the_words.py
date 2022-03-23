
def countwords(list1):
    dic1 = {}
    for word in list1:
        if word not in dic1:
            dic1[word]=1
        else:
            dic1[word]+=1
    print(dic1)


countwords(['pallavi'])


