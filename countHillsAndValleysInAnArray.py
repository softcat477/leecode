from typing import List
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        left_neq = None
        #right_neq = None

        ret = 0
        for idx, num in enumerate(nums):
            # Search for left neq
            left_neq = None
            for j in range(idx-1, -1, -1):
                if nums[j] != num:
                    left_neq = nums[j]
                    break
                break

            # Search for right new
            right_neq = None
            for j in range(idx + 1, len(nums)):
                if nums[j] != num:
                    right_neq = nums[j]
                    break

            # Compare
            if left_neq == None or right_neq == None:
                continue
            l_diff, r_diff = left_neq - num, right_neq - num

            if (l_diff > 0 and r_diff > 0) or (l_diff < 0 and r_diff < 0):
                print (f"found {num}")
                ret += 1

        return ret

sol = Solution()
print (sol.countHillValley([2,4,1,1,6,5]), 3)
print (sol.countHillValley([6,6,5,5,4,1,1,1,1]), 0)
