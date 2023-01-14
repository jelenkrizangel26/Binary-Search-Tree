# Add following methods to BinarySearchTreeNode class created in main video tutorial

# 1. find_min(): finds minimum element in entire binary tree
# 2. find_max(): finds maximum element in entire binary tree
# 3. calculate_sum(): calcualtes sum of all elements
# 4. post_order_traversal(): performs post order traversal of a binary tree
# 5. pre_order_traversal(): perofrms pre order traversal of a binary tree

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

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_me(elements[i])

    return root

if __name__ == '__main__':
    letters = ["J","E","L","E","N","K","R","I","Z","A","N","G","E","L","P","E","R","A","L","T","A","M","A","M","P","U","S","T","I"]
    letters_tree = build_tree(letters)

    print(border)
    print("\33[1m\33[33mLetters\33[0m")
    print("Input letters:",letters)
    print("Min:",letters_tree.find_min())
    print("Max:",letters_tree.find_max())
    print("In order traversal:", letters_tree.in_order_traversal())
    print("Pre order traversal:", letters_tree.pre_order_traversal())
    print("Post order traversal:", letters_tree.post_order_traversal())
    
    print(border)
    print("\33[1m\33[33mNumbers\33[0m")
    numbers = [17,20,15,23,40,25,34,37,89,43,18,14,51]
    numbers_tree = build_tree(numbers)
    print("Input numbers:",numbers)
    print("Min:",numbers_tree.find_min())
    print("Max:",numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    print("In order traversal:", numbers_tree.in_order_traversal())
    print("Pre order traversal:", numbers_tree.pre_order_traversal())
    print("Post order traversal:", numbers_tree.post_order_traversal())
    print("\n")
    
