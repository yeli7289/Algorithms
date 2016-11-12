# Decode Ways
A message containing letters from A-Z is being encoded to numbers using the following mapping:
```
'A' -> 1
'B' -> 2
...
'Z' -> 26
```
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
# Analysis
Dynamic programming

```dp[i+1] = dp[i] or dp[i]+dp[i-1]```, depends on can ```s[i-1:i+1]``` forms a word or not.
# Code
```
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0]=="0":
            return 0
        dp = [0 for i in range(len(s)+1)]
        dp[0], dp[1] = 1, 1
        for i in range(1,len(s)):
            if int(s[i])!=0:
                if 9<int(s[i-1:i+1])<27:
                    dp[i+1] = dp[i]+dp[i-1]
                else:
                    dp[i+1] = dp[i] 
            else:
                if 9<int(s[i-1:i+1])<27:
                    dp[i+1] = dp[i-1]
                else:
                    return 0
        return dp[len(s)]
        
```