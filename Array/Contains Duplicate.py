#IMP making a hashset in which we will put all the array elements turn by turn and if it encounter aduplicatge it willreturn true 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set() #creating a empty hashset
        for n in nums:
            if n in hashset: #if a element is already existing inside the set it will return true 
                return True 
            hashset.add(n) #or else it will continue adding the elements in and return false 
        return False
# time o(n) space O(n)