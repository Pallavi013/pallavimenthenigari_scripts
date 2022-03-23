class Words:

    list1 =['pallavi','pallavi','pooja']

    def Countword(self):
        dic1={}
        for word in self.list1:
            if word not in dic1:
                dic1[word]=1
            else:
                dic1[word]+=1
        print(dic1)

c1= Words()
c1.Countword()

