
def ret_stats(k):
    if (k==None):
        return (0,0)
    w= open("stats.txt","r")
    y=w.readlines()
    print('x')
    x=dict()

    for i in y:
##        print(i)
        if i.startswith(k):
            i.replace('\n', '')
            temp=i.split(" ")
            x[temp[0]]=[int(temp[1]),int(temp[2])]
    return (x,temp[0])


