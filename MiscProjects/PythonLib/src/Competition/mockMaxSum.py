def maximalSum(ratings):
    if len(ratings)==0:
        return 0
    incSum = []
    excSum = []
    if len(ratings)==1:
        if ratings[0]>0:
            return ratings[0]
        else:
            return 0
    if len(ratings) == 2:
        if ratings[0]>0 and ratings[1]>0:
            return ratings[0] + ratings[1]
        else:
            return max(ratings[0],ratings[1])
    incSum.append(ratings[0])
    excSum.append(0)
    incSum.append(max(ratings[0]+ratings[1], ratings[1]))
    excSum.append(ratings[0])
    i=2
    while i<len(ratings):
        incSum.append(max(incSum[-1],excSum[-1]) + ratings[i])
        excSum.append(incSum[-2])
        i+=1
    return max(incSum[-1],excSum[-1])

A = [9,-1,-2,-4,-6,-5,-1,-1]
print maximalSum(A)