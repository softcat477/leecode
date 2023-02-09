class RankOfStream:
    def __init__(self):
        # O(N_hat) space complexity, 
        self.table = {} # number: #number

    def track(self, in_int):
        # O(1) in track
        if in_int not in self.table:
            self.table[in_int] = 0
        self.table[in_int] += 1

    def getRankOf(self, num:int):
        # O(N) in getRankOf
        sorted_keys = sorted(list(self.table.keys()))
        ret_sum = 0
        for key in sorted_keys:
            ret_sum += self.table[key]
            if key == num:
                break
        return ret_sum - 1

sol = RankOfStream()

for i in [5,1,4,4,5,9,7,13,3]:
    sol.track(i)
print(sol.getRankOf(1))
print(sol.getRankOf(3))
print(sol.getRankOf(4))
