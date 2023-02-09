from collections import deque
class WordDictionary:
    class Node:
        def __init__(self):
            self.table = {}
            self.isEnd = False

    def __init__(self):
        self.root = self.Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.table:
                node.table[char] = self.Node()
            node = node.table[char]

        node.isEnd = True

    def search(self, word: str) -> bool:
        queue = deque()
        queue.append((self.root, word))

        while queue:
            node, subword = queue.popleft()

            # print (f"Search {subword} from {node.table.keys()}")

            # end-of-string
            if len(subword) == 0:
                if node.isEnd:
                    return True
                continue
                #return True if node.isEnd else False

            not_found = False
            for idx, w in enumerate(subword):
                if w == ".":
                    # Get wildcard, push children into queue and start the while loop again
                    # to test each children
                    for child in node.table.values():
                        queue.append((child, subword[idx+1:]))
                    not_found = True
                    break
                if w in node.table.keys():
                    node = node.table[w]
                else:
                    # Not match, no need to search more and starts another iteration
                    not_found = True
                    break

            # We've iterate through the whole word -> found
            if not_found != True and node.isEnd:
                return True

        return False

# Your WordDictionary object will be instantiated and called as such:
# sol = WordDictionary()
# 
# sol.addWord("bad")
# sol.addWord("dad")
# sol.addWord("mad")
# 
# print (sol.search("pad"), False)
# print (sol.search("ba"), True)
# print (sol.search("b."), True)
# print (sol.search("."), True)
# print (sol.search("bad"), True)
# print (sol.search(".ad"), True)
# print (sol.search("b.."), True)
# print (sol.search("..."), True)
# print (sol.search(".a."), True)
# print (sol.search(".x."), False)
# print (sol.search("x.."), False)

sol = WordDictionary()

sol.addWord("at")
sol.addWord("and")
sol.addWord("an")
sol.addWord("add")
print (sol.search("a"), False) # HERE
print (sol.search(".at"), False)
sol.addWord("bat")
print (sol.search(".at"), True)
print (sol.search("an."), True)
print (sol.search("a.d."), False)
print (sol.search("b."), False) # HERE
print (sol.search("a.d"), True)
print (sol.search("."), False) # HERE

sol = WordDictionary()
sol.addWord('xgvk')
sol.addWord('wykzbvwdsoyfowqicymzd')
sol.addWord('xajbtjyjuwgoynjgu')
sol.addWord('qsibzxaorktypkfg')
sol.addWord('vbycuvrkbcq')
sol.addWord('sm')
sol.addWord('fkqclfmvzpzpnbvz')
sol.addWord('jpnneostllnnma')
sol.addWord('zvmtfg')
sol.addWord('lboe')
sol.addWord('jypzkxnzc')
sol.addWord('qes')
sol.addWord('jioqlytzqx')
sol.addWord('fojsjyiz')
sol.addWord('qkprluekewtsftvbrjndpt')
sol.addWord('mwsgyywmmkzmy')
sol.addWord('tcjmitm')
sol.addWord('pybk')
sol.addWord('poljqcitty')
sol.addWord('qfdabgsvkboyaq')
sol.addWord('pvreuprpvoycadnsxaajrkh')
sol.addWord('sv')
sol.addWord('knmxzabetvqehv')
sol.addWord('ziazu')
sol.addWord('ghhelrzgbsmxkrnezif')
sol.addWord('fn')
sol.addWord('tnjcttrsozynjpqhox')
sol.addWord('qhxcfujxmayzlsrctmsa')
sol.addWord('fyaaivfrupktdgw')
print (sol.search("..."), True)
