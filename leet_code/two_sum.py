class Solution(object):
    def twoSum(self, target, *nums):
        seen={}
        for i, v in enumerate(*nums):
            remaining=target-v
            if remaining in seen:
                return[seen[remaining],i]
            seen[v]=i
        return []
obj1=Solution()
print(obj1.twoSum(9 ,2,7,11,15))