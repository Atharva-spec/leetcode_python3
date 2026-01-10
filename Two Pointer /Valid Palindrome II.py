#flow same as valid palindrome, if encounter a miss match skip both the char one by one n check by reversing the str if same if palindrome if not then not a palindrome

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                skipleft, skipright = s[left + 1 : right + 1], s[left:right]
                return (skipleft == skipleft [:: -1] or skipright == skipright[:: -1])
                #[::-1] helps in reversing a string
            left +=1
            right -= 1
        return True 