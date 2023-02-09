from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def isOverlap(_interval, _newInterval):
            if _newInterval == None:
                return False
            isLeft = _interval[1] < _newInterval[0]
            isRight = _interval[0] > _newInterval[1]
            return (isLeft == False) and (isRight == False)

        ret = []
        hasEnterMerge = False
        for interval in intervals:
            if isOverlap(interval, newInterval):
                new_head = min(interval[0], newInterval[0])
                new_tail = max(interval[1], newInterval[1])
                newInterval = [new_head, new_tail]
                hasEnterMerge = True
            else:
                if hasEnterMerge == True and newInterval != None:
                    ret.append(newInterval)
                    newInterval = None
                else:
                    if newInterval != None and newInterval[1] < interval[0]:
                        ret.append(newInterval)
                        newInterval = None
                ret.append(interval)

        if newInterval != None:
            ret.append(newInterval)
        return ret

sol = Solution()

intvl = [[1,3],[6,9]]
new_intvl = [2,5]
print (sol.insert(intvl, new_intvl), [[1,5],[6,9]])

intvl_1 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
new_intvl_1 = [4,8]
print (sol.insert(intvl_1, new_intvl_1), [[1,2],[3,10],[12,16]])

intvl_2 = [[1,2],[3,4],[7,8],[9,10],[12,16]]
new_intvl_2 = [5,6]
print (sol.insert(intvl_2, new_intvl_2), [[1,2],[3,4],[5,6],[7,8],[9,10],[12,16]])

intvl_3 = [[1,2],[3,12],[13,14]]
new_intvl_3 = [5,6]
print (sol.insert(intvl_3, new_intvl_3), [[1,2],[3,12],[13,14]])

intvl = [[1,3],[6,9]]
new_intvl = [3,5]
print (sol.insert(intvl, new_intvl), [[1,5],[6,9]])

intvl = [[1,3],[6,9]]
new_intvl = [4,7]
print (sol.insert(intvl, new_intvl), [[1,3],[4,9]])

intvl = [[1,3],[6,9]]
new_intvl = [2,7]
print (sol.insert(intvl, new_intvl), [[1,9]])

intvl = [[1,3],[6,9],[10,12]]
new_intvl = [2,7]
print (sol.insert(intvl, new_intvl), [[1,9],[10,12]])
