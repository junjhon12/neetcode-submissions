class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        newdict={}
        res=0
        maxf=0
        l=0

        for r in range(len(s)):
            newdict[s[r]]= newdict.get(s[r],0)+1
            maxf= max(maxf, newdict[s[r]])

            while (r-l+1)-maxf>k:
                newdict[s[l]]=newdict[s[l]]-1
                l=l+1

            res=r-l+1
        return res