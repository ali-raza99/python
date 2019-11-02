def readfile(da):
    num=[]

    with open(r"C:\Users\Tayyab\Desktop\"",da,".txt") as f:
        for item in f:
            for i in item:
                num.append(i)

    return num

arr= readfile("a")
print(arr)

