rows = 5
columns = 5

for i in range(0,rows+1):
    for j in range(columns-i,0,-1):
        print(j,end=" ")
    print()