class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        #arrow in function parameters means expected return
        if len(s) != len(t): 
        #if the length of s is different from t, no way they can be     anagrams
            return False
        counterS, counterT = {}, {}
        #create words dictionaries, null

        for i in range(len(s)): #strings must use the len function to iterate through their characters
            counterS[s[i]] = 1 + counterS.get(s[i], 0)
            #each key in the counterS directory will get its value from checking the existence of the said key in the directory "counterS.get(s[i])". If the key "i" does not exist yet, safely return 0, and add 1 so you understand key value only shows once. If we check the existence of the same key a second time, now we add to the existing value 1, sum 1, we have two. The key updates. And so on. 
            counterT[t[i]] = 1 + counterT.get(t[i], 0)

        for c in counterS: 
            #each key-value pair in directory counterS
            if counterS[c] != counterT.get(c, 0):
                #if the iterated key-value pair in counterS does not show up anywhere in counterT, will return zero, which returns a true difference (if it exists in counterS it cannot not exist in counterT). If it shows up but a different value than the one in counterS ("a":1, "a": 2), is a true difference as well.
                return False

        return True 
        #other than that, it should be true that it is an anagram. Easier to clear out when is not.

