class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        o=''
        s=strs[0] 
        w=strs[len(strs)-1]
        for i in range(len(min(s,w))):
            if(s[i]==w[i]):
                o+=s[i]
            else:
                break
        return o
        