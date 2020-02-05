import pandas as pd
import sys
arg0=sys.argv
df=pd.read_csv(arg0[1],header=None)
df=df.fillna("notfound")
def functionback(n):
    if n>=df.shape[0]:
        l=[""]
        return l
    nex=functionback(n+1)
    ans=[]
    for i in df.iloc[n]:
        for j in nex:
            if i!='notfound' and j!='notfound':
                ans.append(str(i)+str(j))
    ans=list(filter(lambda a:a!='notfound',ans))
    return ans
l=functionback(0)
for i in range(len(l)-1):
    print(l[i],end=',')
print(l[len(l)-1])
