"""
Write a function to see if a binary tree ↴ is "superbalanced" 
(a new tree property we just made up).
A tree is "superbalanced" if the difference between the depths 
of any two leaf nodes ↴ is no greater than one.
"""
def is_balanced(tree_root):
    #a tree with no nodes is super balanced since there are no leaves
    if tree_root is None:
        return True

    #we short circuit as soon as we find more than 2
    depths = []

    #we'll treat this as a stack that will store tuples 
    #of (node, depth)
    nodes = []
    nodes.append(tree_root, 0)

    while len(nodes):
        node, depth = nodes.pop()

        #case we found a leaf
        if not node.left and not node.right:
            if depths not in depths:
                depths.append(depth)

            if len(depths) > 2 or 
                len(depths) == 2 and abs(depths[0] - depths[1] > 1):
                return False

        else:
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))

    return True
"""
Write a function to check that a binary tree
 is a valid binary search tree.
"""
def is_binary_search_tree(root):
    node_and_bounds_stack = [(root, -float('inf'), float('inf'))]

    while len(node_and_bounds_stack):
        node, lower_bound, upper_bound = node_and_bounds_stack.pop()

        if node.val < lower_bound or node.val > upper_bound:
            return False

        if node.left:
            node_and_bounds_stack.append((node.left, lower_bound, node.val)) 

        if node.right:
            node_and_bounds_stack.append((node.right, node.val, upper_bound))

    return True