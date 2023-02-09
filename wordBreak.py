from typing import List, Dict
class Solution:
    def recSolve(self, sub_s: str, memory: Dict[str, int]) -> bool:
        if len(sub_s) == 0:
            return True
        wordDict = self.wordDict

        # Parse sub_s and find all the matching word
        for word_len in range(1, self.max_word_len + 1): # 1 ~ max_word_len
            word = sub_s[:word_len]

            # This word exists in dict, so we either dive down or read from memory
            # to know if its postfix can also be decomposed into words
            if word in wordDict:
                new_sub_s = sub_s[word_len:]

                if new_sub_s not in memory:
                    # dive down only if the sub_s is not in memory
                    can_decompose = self.recSolve(new_sub_s, memory)
                    # and add result to memory
                    memory[new_sub_s] = can_decompose

                # Read the result from cache
                can_decompose = memory[new_sub_s]
                if can_decompose:
                    # As long as there's one solution (word + sub_string that can be decomposed), we return True
                    #ret = True
                    return True

        return False



    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = wordDict
        max_word_len = max([len(w) for w in wordDict])
        self.max_word_len = max_word_len

        mem = {}
        ans = self.recSolve(s, mem)
        return ans

sol = Solution()

print (sol.wordBreak("leetcode", ["leet", "code"]), True)
print (sol.wordBreak("leetcode", ["leetcode"]), True)
print (sol.wordBreak("applepenapplepen", ["apple", "pen"]), True)
print (sol.wordBreak("casandog", ["cats", "dog", "sand", "and", "cat"]), False)
print (sol.wordBreak("catcatcatcatcat", ["cat"]), True)
print (sol.wordBreak("catcatcatcatcat", ["cat", "atc"]), True)
print (sol.wordBreak("catcatcatcatcat", ["atc", "c", "at"]), True)
print (sol.wordBreak("catcatcatcatcat", ["atc"]), False)
