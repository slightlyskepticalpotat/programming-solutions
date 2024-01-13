class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(src, dest, path):
            if not dest:
                ans.append(path.copy())
                return
            for i in range(src, len(candidates)):
                if dest - candidates[i] < 0:
                    continue
                path.append(candidates[i])
                dfs(i, dest - candidates[i], path)
                path.pop()
        candidates.sort()
        dfs(0, target, [])
        return ans