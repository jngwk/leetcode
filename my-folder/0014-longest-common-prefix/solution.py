class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # start with first word, compare from the first index
        # if the last index of the first word exists
        lcp = strs[0]
        # print(strs[0][0])
        for i in range(1, len(strs)):
          idx = 0
          len_of_str = len(strs[i])
          len_of_lcp = len(lcp)

          while len_of_str > idx and len_of_lcp > idx and strs[i][idx] == lcp[idx]:
            idx += 1
          
          lcp = lcp[0:idx]
        
        return lcp

