from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        n, m, w = len(s), len(words), len(words[0])
        need = Counter(words)
        res = []

        for off in range(w):                  # each alignment
            left = off
            seen = {}
            count = 0                         # words currently in window
            for right in range(off, n - w + 1, w):
                word = s[right:right + w]
                if word in need:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1
                    while seen[word] > need[word]:   # too many of this word
                        lw = s[left:left + w]
                        seen[lw] -= 1
                        count -= 1
                        left += w
                    if count == m:            # valid window
                        res.append(left)
                        lw = s[left:left + w]
                        seen[lw] -= 1         # slide by one word
                        count -= 1
                        left += w
                else:                         # bad word, reset window
                    seen.clear()
                    count = 0
                    left = right + w
        return res