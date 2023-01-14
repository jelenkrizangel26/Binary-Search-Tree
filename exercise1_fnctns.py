border = ("\n\33[34m**********************************************************************\33[0m\n")

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

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

def build_tree(elements):
    print("\nBuilding tree with these elements: ",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_me(elements[i])

    return root

if __name__ == '__main__':
    letters = ["J","E","L","E","N","K","R","I","Z","A","N","G","E","L","P","E","R","A","L","T","A","M","A","M","P","U","S","T","I"]
    letters_tree = build_tree(letters)

    print(border)
    print("\33[1m\33[33mLetters\33[0m")
    print("Does letter C is on the list?", letters_tree.search("C"))