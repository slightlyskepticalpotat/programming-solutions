class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs, ans, loc = [("".join(sorted(list(i))), i) for i in strs], [], []
        strs.sort()
        while strs:
            if not loc:
                loc.append(strs.pop())
            elif strs[-1][0] == loc[-1][0]:
                loc.append(strs.pop())
            else:
                ans.append(loc)
                loc = []
        if loc:
            ans.append(loc)            
        return [[j[1] for j in i] for i in ans]