from typing import List
import copy

def getPeakOrValley(nums: List[int], LR) -> int:
    # Search peaks, return its position if found
    l, r = LR
    while True:
        if r < l:
            break
        if l == r:
            # Boundary does not count
            if l == 0 or r == len(nums) - 1:
                break
            if nums[l] > nums[l-1] and nums[l] > nums[l+1]:
                # Found a peak
                return l
            else:
                # Nothing here
                break
        mid = (l + r) // 2 
        # print (f" Peak Range : {l} - {r} mid: {mid}")
        if mid == 0 or mid == len(nums) - 1:
            break
        if (nums[mid] - nums[mid - 1]) * (nums[mid + 1] - nums[mid]) < 0:
            # print (f" Peak at {mid}")
            return mid
        if (nums[mid] - nums[mid - 1]) < 0:
            r = mid - 1
        else:
            l = mid + 1

    # Search valley, return its position if found
    l, r = LR
    while True:
        print (f"l/r : {l}/{r}")
        if r < l:
            break
        if l == r:
            # Boundary does not count
            if l == 0 or r == len(nums) - 1:
                break
            if nums[l] < nums[l-1] and nums[l] < nums[l+1]:
                # Found a peak
                # print (f"Valley")
                return l
            else:
                # Nothing here
                break
        mid = (l + r) // 2 
        print (f"Valley Range : {l} - {r} mid: {mid}")
        # If this is a peak
        if mid == 0 or mid == len(nums) - 1:
            break
        if (nums[mid] - nums[mid - 1]) * (nums[mid + 1] - nums[mid]) < 0:
            # print (f"valley")
            return mid
        if (nums[mid] - nums[mid - 1]) > 0:
            r = mid - 1
        else:
            l = mid + 1

    # Lastly, return -1 since there's no peaks or valleys inside.
    # print ("Not found")
    return -1

def solution(nums:List[int]) -> int:
    
    # 1. Use the whole array to get the position of either a peak or valley
    #    there could be multiple peaks or valleys, which are invalid cases
    pv_idx = getPeakOrValley(nums, (0, len(nums) - 1))
    # TODO: No peaks or valleys
    if pv_idx == -1:
        return -1

    # 2. the LHS of pv_idx, should get no peaks
    # print ("\nSearch LEFT")
    invalid_pv_idx = getPeakOrValley(nums, (0, pv_idx - 1))
    # TODO: Found more peaks on the left
    if invalid_pv_idx != -1:
        return -1

    # 2. the RHS of pv_idx, should get no peaks
    # print ("\nSearch RIGHT")
    invalid_pv_idx = getPeakOrValley(nums, (pv_idx + 1, len(nums) - 1))
    # TODO: Found more peaks on the right
    if invalid_pv_idx != -1:
        return -1

    # TODO: Return positions
    return pv_idx

# print (solution([3,2,1,0,1]), 3)
# print (solution([4,5,6,7,8,9,8,7]), 5)
# print (solution([1,2,3]), -1)
# print (solution([1,2,3,2,1,2]), -1)
print (solution([7,5,4,3,4,3]), -1)
