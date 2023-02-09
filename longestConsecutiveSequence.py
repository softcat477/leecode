from typing import Dict, List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # table[num] = does num connected to the next number
        table: Dict[int, bool] = {i:False for i in nums}

        for num in nums:
            if num + 1 in table:
                table[num] = True
            else:
                table[num] = False

            if num - 1 in table:
                table[num - 1] = True

        # Dive down
        ret_max = 1
        for num in table.keys():
            hasNext = table[num]

            if type(hasNext) == bool and hasNext == False:
                table[num] = 1
                continue
            if type(hasNext) == int:
                continue

            # Dive down to get the length
            length = 0 # Starts from num to the last connected num (the one marked as false)
            _num = num # the last connected num
            while _num in table:
                length += 1

                # Does not connected to the next element
                content = table[_num]
                if type(content) == int or (type(content) == bool and content == False):
                    break

                # Mark as processed
                table[_num] = False

                # Dive down
                _num = _num + 1

            # The last connected num has been processed and has its longest connected length
            if _num in table and type(table[_num]) == int:
                length = length + table[_num] - 1

            #longest_length[num] = length
            table[num] = length
            ret_max = max(length, ret_max)

        return ret_max

sol = Solution()

nums1 = [100,4,200,1,3,2]
nums2 = [8,3,7,2,5,0,4,6,0,1]
nums3 = [40,2,4,6,8,10,39]
nums4 = [40,2,4,6,8,10]
nums5 = [40]
nums6 = []

print (sol.longestConsecutive(nums1), 4)
print (sol.longestConsecutive(nums2), 9)
print (sol.longestConsecutive(nums3), 2)
print (sol.longestConsecutive(nums4), 1)
print (sol.longestConsecutive(nums5), 1)
print (sol.longestConsecutive(nums6), 0)
# print (sol.longestConsecutive())
# print (sol.longestConsecutive())
# print (sol.longestConsecutive())
# print (sol.longestConsecutive())
# print (sol.longestConsecutive())
