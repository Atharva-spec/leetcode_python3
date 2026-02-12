class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k

        while l < r:
            m = (l+r) // 2
            if x - arr[m] > arr[m + k] - x:
                l =  m + 1
            else:
                r = m
        return arr[l:l+k]

    # x = the target value
    # k = the number of value closest to it (condition always go with the value less than the taget value)