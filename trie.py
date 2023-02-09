class Trie:
    class Node:
        def __init__(self, char:str = ""):
            self.char = char
            self.children = {}
        def addChild(self, child, char: str):
            # Add <char> to its children
            self.children[char] = child
        def hasChild(self, char: str) -> bool:
            # Return True if <char> is in its children table
            return char in self.children.keys()
        def getChild(self, char: str):
            # Return the children with val = <char>
            return self.children[char]
        def isLeaf(self) -> bool:
            return len(self.children) == 0
        def __str__(self):
            keys = list(self.children.keys())
            ret_str = ", ".join(keys)
            return ret_str


    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        # Recursively insert nodes representing each character in <word>
        # If a character already exists, dive down
        current_node = self.root
        for char in word:
            if current_node.hasChild(char) == False:
                # A node with val = <char> does not exists, we have to create one and dive down
                # print (f"Insert {char} to node: {current_node.char}")
                new_node = self.Node(char)
                current_node.addChild(new_node, char)
            current_node = current_node.getChild(char)

        # Insert a terminate char
        current_node.addChild(self.Node("NULL"), "NULL")
        

    def search(self, word: str) -> bool:
        # Search the whole word
        # Iterate through each characters in word.
        # All characters should be found in the tree, or else we immediatly return False

        current_node = self.root
        for char in word:
            if current_node.hasChild(char) == False:
                return False
            current_node = current_node.getChild(char)

        # Need to have a terminate char
        if current_node.hasChild("NULL") == True:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        # Only search the prefix
        current_node = self.root
        for char in prefix:
            if current_node.hasChild(char) == False:
                return False
            current_node = current_node.getChild(char)

        # It doesn't matter if we're at a leaf node or not, as long as we found the whole prefix,
        # we can return True
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

tree = Trie()
tree.insert("apple")
print (tree.search("apple"), True)
print (tree.startsWith("a"), True)
print (tree.search("app"), False)
print (tree.startsWith("app"), True)
print (tree.startsWith("apple"), True)
tree.insert("app")
print (tree.search("app"), True)
print (tree.startsWith("app"), True)
print (tree.startsWith("apple"), True)

tree.insert("prefix")
print (tree.search("app"), True)
print (tree.startsWith("app"), True)
print (tree.startsWith("apple"), True)
print (tree.search("prefix"), True)
print (tree.search("p"), False)
print (tree.startsWith("p"), True)
print (tree.startsWith("pre"), True)
print (tree.startsWith("prefix"), True)


tree = Trie()
print (tree.search("p"), False)
print (tree.startsWith("prefix"), False)
