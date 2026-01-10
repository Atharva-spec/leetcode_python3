#concatenation of array (two small strings are connected into one larger string)
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [] #empty array for ans
        for i in range(2):
            for num in nums:
                ans.append(num) #append adding an element at the last of the list inside the array 
        return ans