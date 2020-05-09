T = int(input("T = "))

while T < 1 or T > 100:
    print("1<=T<=100")
    T = int(input("T = "))

for i in range(T):
    A = int(input("A = "))
    B = int(input("B = "))
    s = 0
    while A < 1 or B < 1 or A > 10 ** 9 or B > 10 ** 9:
        print("1<=A,B<=10^9")
        A = int(input("A = "))
        B = int(input("B = "))

    if A + B > 10:
        s += A + B - 10


    print("Az osszeg = {}".format(s))
