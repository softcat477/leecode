from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])

        discard = 0
        #tail = intervals[0][1]
        head, tail = intervals[0]
        for intvl in intervals[1:]:
            if intvl[0] < tail:
                discard += 1
                if intvl[1] > tail:
                    continue
            tail = intvl[1]

        return discard

sol = Solution()

func = sol.eraseOverlapIntervals

print (sol.eraseOverlapIntervals([[-25322,-4602],[-35630,-28832],[-33802,29009],[13393,24550],[-10655,16361],[-2835,10053],[-2290,17156],[1236,14847],[-45022,-1296],[-34574,-1993],[-14129,15626],[3010,14502],[42403,45946],[-22117,13380],[7337,33635],[-38153,27794],[47640,49108],[40578,46264],[-38497,-13790],[-7530,4977],[-29009,43543],[-49069,32526],[21409,43622],[-28569,16493],[-28301,34058]]
), 19)


print (sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]), 1)
print (sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]]), 2)
print (sol.eraseOverlapIntervals([[1,2],[2,3]]), 0)
print (sol.eraseOverlapIntervals([[1,2]]), 0)
print (sol.eraseOverlapIntervals([[1,5], [1,3], [3,5], [1,2], [2,3], [3,4], [4,5]]), 3)
