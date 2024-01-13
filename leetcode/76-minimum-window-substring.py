class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt, ans_i, ans_j, i, j = defaultdict(int), 0, float("inf"), 0, 0
        for char in t:
            cnt[char] += 1
        while j < len(s):
            if s[j] in cnt: # move right ptr
                cnt[s[j]] -= 1
            j += 1
            if all(i < 1 for i in cnt.values()): # if valid window
                while True: # move left ptr
                    if s[i] not in cnt:
                        i += 1
                    elif cnt[s[i]]:
                        cnt[s[i]], i = cnt[s[i]] + 1, i + 1
                    else:
                        break                    
                if ans_j - ans_i > j - i:
                    ans_i, ans_j = i, j
                    cnt[s[i]], i = cnt[s[i]] + 1, i + 1 # search for new window
        try:
            return s[ans_i:ans_j]
        except:
            return ""