#Activity from the vid and the exercise 2

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

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

def build_tree(elements):
    print("Building tree with these elements: ",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_me(elements[i])

    return root

if __name__ == '__main__':
    letters = ["J","E","L","E","N","K","R","I","Z","A","N","G","E","L","P","E","R","A","L","T","A","M","A","M","P","U","S","T","I"]
    letters_tree = build_tree(letters)

    numbers = [17,20,15,23,40,25,34,37,89,43,18,14,51]
    numbers_tree = build_tree(numbers)