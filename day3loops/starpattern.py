rows = 4

for i in range(1, rows+1):
    # print spaces
    print(" " * (rows - i), end="")
    # print stars
    print("*" * (2*i - 1))
