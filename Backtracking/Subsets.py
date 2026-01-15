#using recurstion we will get n^2 answer
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            while i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i]) #this includes nums[i] to the tree (left branch)
            dfs(i + 1)

            subset.pop() #this excludes nums[i] to the tree (right branch)
            dfs (i + 1)
        
        dfs (0) 
        return res 