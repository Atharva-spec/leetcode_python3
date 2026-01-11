class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            #to find max area just multiply them both
            res = max(res, area)

            if height[l] <= height[r]:
                l += 1 #if left is smaller move left pointer
            else:
                r -= 1 #if right is smaller move right pointer
        return res #returning the max area