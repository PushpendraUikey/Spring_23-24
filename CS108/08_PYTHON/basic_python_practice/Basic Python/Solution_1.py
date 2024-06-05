import sys

file=sys.argv[1]

k_series_list=[2,3,5,5,7,7]
def isPrime(n):
    if n == 1:
        return False
    else:
        for num in range(2,n):
            if n%num==0:
                return False
    return True

def Update_K_series(oldMx, newMax):
    i = k_series_list[oldMx-1] +1
    while oldMx<newMax:
        if isPrime(i-2) and isPrime(i):
            k_series_list.append(i)
            oldMx+=1
            i+=1
        else:
            while not isPrime(i):
                i+=1
            k_series_list.append(i)
            oldMx+=1

num = []
with open(file) as input:
    lines = input.readlines()            # readlines() function makes the list of input's files lines.
    for line in lines:
        num.append(int(line))

queury = num.pop(0)
oldMax = 6
for i in num:
    if(i>oldMax):
        Update_K_series(oldMax,i+2)
        oldMax=i+2
    print(k_series_list[i-1])
