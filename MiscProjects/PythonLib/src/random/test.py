n1,n2 = [int(i) for i in raw_input().split(' ')]

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

print gcd(15,10)
count = 0
d = 1
while d <= n1/2:
    if n1%d==0 and n2%d==0:
        count+=1
    d += 1
    
print count

def maxSubArr(arr):
    maxSum = 0
    maxSumSoFar = 0
    maxEndsHere = 0
    for i in range(len(arr)):
        maxSumSoFar += arr[i]
        if maxSumSoFar > maxSum:
            maxEndsHere = i
            maxSum = maxSumSoFar
        if maxSumSoFar<0:
            maxSumSoFar = 0
            maxEndsHere = i
    return maxSum

arr = [-2,-1,4,-1,-6,1,5,-3]
print maxSubArr(arr)

def repeatedStringMatch(A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        ind = 1
        cur = A
        while len(cur) < len(B):
            cur = cur + A
            ind += 1
            if cur.find(B)>=0:
                return ind
        if cur.find(B)>=0:
            return ind
        cur = cur + A
        ind += 1
        if cur.find(B)>=0:
            return ind
        else:
            return -1
        
print repeatedStringMatch("abcd","cdabcdab")
