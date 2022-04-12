def gotyou():
    for x in range(1,116):
        if x%2==0 and x%11==0:
            print("got you")
        elif x%2==0:
            print("got")
        elif x%11==0:
            print("you")
        else:
            print(x)

gotyou()