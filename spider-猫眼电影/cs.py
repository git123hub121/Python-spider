a = [[1,2,3,4,5],[2,4,5,8,9]]
b = []
for i in a:
    i1 = i[3]+i[4]
    print(i1)
    b = i[:3]
    b.append(i1)
    print(b)
