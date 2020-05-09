import random
N=int(random.randint(1,10000))
print(N)
szam=0
nyertes=""
lst=[]
lst2=[]
maxkulombseg=0
maxh=""

while szam<=N:
    P1 = int(random.randint(1, 1000))
    P2 = int(random.randint(1, 1000))
    print("P1={} P2={}".format(P1, P2))

    kulombseg=0
    if P1>P2:
        kulombseg+=P1-P2
        szam+=1
        lst.append(kulombseg)
        nyertes="P1"
        lst2.append(nyertes)
        print("A kört P1 nyerte {} ponttal".format(kulombseg))
    elif P2>P1:
        kulombseg+=P2-P1
        szam+=1
        lst.append(kulombseg)
        nyertes="P2"
        lst2.append(nyertes)
        print("A kört P2 nyerte {} ponttal".format(kulombseg))
    else:
        szam+=1
        print("A kör döntetlen lett")



for i in range(len(lst)):
    if lst[i]>maxkulombseg:
        maxkulombseg=lst[i]
        maxh=lst2[i]

print("A versenyt a legnagyobb külömbséggel={}, {} nyerte!".format(maxkulombseg,maxh))