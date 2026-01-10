class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase_s = s.lower() #all uppercase char into lower 
        left = 0 #pointer no.1 starts from the start of the string
        right = len(s) - 1 #pointer no.2 starts from the end of the string
        
        while left < right:
           
            while left < right and not self.alphaNum(s[left]): 
                #will skipp all the junk
                left += 1
            while left < right and not self.alphaNum(s[right]): 
                #will skip all the junk
                right -= 1
            if s[left].lower() != s[right].lower(): 
                #if letters dont match return false
                    return False        
            left += 1
            right -= 1
        return True
    def alphaNum(self,  c):
        return c.isalnum() #build in string method 
