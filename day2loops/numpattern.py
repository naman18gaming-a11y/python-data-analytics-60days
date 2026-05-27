# print num  pattern
n = int (input("enetr the number of rows:"))
rows = n
for i in range (1,rows+1):
    for j in range ( 1,i+1):
        print(j,end="")
    print() 
    