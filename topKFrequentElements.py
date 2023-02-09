from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _table = {num:0 for num in nums}
        for num in nums:
            _table[num] += 1

        table: List = list(_table.items())
        table = sorted(table, key=lambda x: x[-1])

        ret = []
        while k - len(ret) > 0:
            ret.append(table.pop()[0])

        return ret

sol = Solution()

print (sol.topKFrequent([1,1,1,2,2,3], 2), [1,2])
print (sol.topKFrequent([1], 1), [1])
