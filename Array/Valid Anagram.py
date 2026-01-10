#Anagram use the same words of a sentence and rearranging them and making it into one new sentence 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #*!=* means not equal to 
            return False 
            
        countS={} #these are our dictionarys 
        countT={} #to count the no.of elements in both the strings 

        for i in range(len(s)): #i is the index for both str
            countS[s[i]] = 1 + countS.get(s[i], 0) # working of GET statement *dictionary.get(key, default_value)* if exist in hashmap returns 1 or else 0 as default value
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS: #for counts in the hashmap
            if countS[c] != countT.get(c,0): #if counts are not the same 
                return False 
        
        return True 