class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        res = ""
        # Iterate through the characters of the first string
        for i in range(len(strs[0])):
            # Check the character at index i against all other strings
            for s in strs:
                # If index i is out of bounds for string s OR 
                # the character in s doesn't match the character in the first string (strs[0])
                if i == len(s) or s[i] != strs[0][i]:
                    return res  # Prefix ends here, return the accumulated result
            # If the inner loop completes, it means strs[0][i] is common to all
            # CORRECTED: Append the character at the CURRENT index 'i'
            res += strs[0][i] 
            
        return res