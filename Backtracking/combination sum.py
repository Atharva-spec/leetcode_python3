class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs (i, cur, total):
            if (total == target): #if matches add
                res.append(cur.copy())
                return 
            if i >= len(candidates) or total > target: 
                #if i goes out of bounde or total greater 
                return 

            cur.append(candidates[i]) #to avoid repeated outputs
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0) #funcation call
        return res