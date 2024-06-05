import sys

num=int(sys.argv[1])
k=10**9+7
def countWays(n):
    res = [0] * (n + 1)
    res[0] = 1
    res[1] = 1
    res[2] = 2
 
    for i in range(3, n + 1):
        res[i] = res[i - 1] + res[i - 2] + res[i - 3]
 
    return res[n]
 
 
# Driver code
n = 4
print(countWays(n))