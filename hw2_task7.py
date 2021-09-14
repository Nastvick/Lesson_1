#rows = int(input("How many rows:? "))
#columns = int(input("How many columns:? "))
#symbol = input("Enter a symbol to use: ")

#for i in range(rows):
    #for j in range(columns):
        #print(symbol, end="")
    #print()

for num in range(7):
    for i in range(num):
        print("*", end=" ")
    print()


rows = 5
columns = 5

for i in range(0,rows+1):
    for j in range(columns-i,0,-1):
        print("*",end=" ")
    print()

