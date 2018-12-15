import random
computer = random.randint(10)
user = 1
i = 0
sum = 0
while i <= 100 :
    if i % 2 == 0:
        sum = sum + i
    i += 1
print(sum)

su = 0

# 递归

def recursion(k):
    """注释"""
    if k == 0:
        return su
    return k + recursion(k-1)
# print(recursion(100))

# Sn=n(a1+an)/2
def sumA(n):
    return(n*(n+1)/2)

# 乘法表
def mul(mu):
    row = 1
    while row <= mu:
        col = 1
        while col <= row:
            print("%d\t*\t%d= %d\t\t" % (row, col, row*col), end = "")
            col += 1
        print("")
        row += 1
mul(20)