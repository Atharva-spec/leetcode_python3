class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
       
        def dfs (i, total): 
            if i == len(nums): #if we have reached the end of the array
                return total
            
            return dfs(i + 1, total ^ nums[i]) + dfs(i + 1, total) #recursive call

        return dfs(0, 0) 