/*
  LOngest subStirng with no repeating characters
  below sliding window techinque 
  O(N) Time complexity
  O(N) space 
  Appeared in LeetCode under Google explorer
*/

class Solution(object):
    def lengthOfLongestSubstring(self, s):

        res = 0 
        left = 0  
        c2index = {}    # record the latest index of char
        for i,c in enumerate(s):
            if c in c2index and c2index[c]>=left:
                left = c2index[c]+1   # assign a new left (new start position)
    
            c2index[c] = i   # recording latest index of char
            res = max(i-left+1,res)    
        return res
