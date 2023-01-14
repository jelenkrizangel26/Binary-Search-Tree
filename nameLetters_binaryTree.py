#Making the lesson on the first vid using my name as the string: JELEN KRIZ ANGEL PERALTA MAMPUSTI
#Will include the search and in order traversal.

class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    #for if node already exist it would not repeat it
    def add_me(self, data):
        if data == self.data:
            return 
    #For the left and right subtree
        if data < self.data:
            if self.left:
                self.left.add_me(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_me(data)
            else:
                self.right = BinarySearchTreeNode(data)
