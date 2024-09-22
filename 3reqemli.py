print("3 reqemli eded daxil edin")

abc = int(input())

if(99 < abc < 1000):
    c = abc % 10
    ab = abc // 10
    b = ab % 10
    a = ab // 10

    if (a == 0 and b != 0 and c != 0 or b == 0 and c != 0 and a != 0 or c == 0 and b != 0 and a != 0):
        print("4")
    elif (a == b == c or a == 0 and b == 0 or b == 0 and c == 0 or a == 0 and c == 0):
        print("1")
    elif (a == b or b == c or a == c):
        print("3")
    else:
        print("6")
else:
    print("daxil etdiyiniz reqem 3 reqemli deyil")