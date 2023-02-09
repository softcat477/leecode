from typing import List
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return len(nums)
        if len(nums) == 2:
            return 2 if nums[0] != nums[1] else 1

        # Must include head
        idx = 1
        seq_len = 1

        idx = 0
        while  nums[idx] == nums[idx + 1]:
            idx += 1
            if idx + 1 == len(nums):
                return 1
        #print (f"idx:{idx}")
        p_diff = nums[idx+1] - nums[idx]
        idx += 1
        while idx != len(nums) - 1:
            n_diff = nums[idx + 1] - nums[idx]
            #print (f"{p_diff} {nums[idx]} {n_diff}")
            if p_diff * n_diff < 0:
                # This is a wiggling part, add this to the subsequence
                seq_len += 1
                p_diff = n_diff
            else:
                # We move forward until we found a wiggling part
                idx += 1

        # Must include tail
        if seq_len == 1 and nums[0] == nums[-1]:
            return seq_len
        else:
            seq_len += 1
            return seq_len

sol = Solution()

nums1 = [1,7,4,9,2,5]
nums2 = [1,17,5,10,13,15,10,5,16,8]
nums3 = [1,2,3,4,5,6,7,8,9]

nums4 = [1,17,5,10,13,15,10,5,16,17,18,19]

print (sol.wiggleMaxLength(nums1), 6)
print (sol.wiggleMaxLength(nums2), 7)
print (sol.wiggleMaxLength(nums3), 2)
print (sol.wiggleMaxLength(nums4), 6)
print (sol.wiggleMaxLength([0,0]), 1)
print (sol.wiggleMaxLength([1,0]), 2)
print (sol.wiggleMaxLength([0,0,0,0,0,0]), 1)
print (sol.wiggleMaxLength([2,2,2,5,0]), 3)
print (sol.wiggleMaxLength([1,0,0,0,0]), 2)
print (sol.wiggleMaxLength([1,0,0,0,1]), 3)
