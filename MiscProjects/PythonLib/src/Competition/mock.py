def subsets(A):
        A.sort()
        res = [[]]
        for i in A:
            tempRes = []
            for j in res:
                tempj = j + [i]
                tempRes.append(tempj)
            tempRes.reverse()
            res = res + tempRes
        return res
    
print subsets([1,2])