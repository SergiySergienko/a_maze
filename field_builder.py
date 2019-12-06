def addNode(node, currentXIndex, currentYIndex):
    if currentXIndex > 0:
        n = Node(False, False)
        n.right = node
        node.left = addNode(n, currentXIndex - 1, currentYIndex)
    else:
        return -1

    if currentYIndex > 0:
        n = Node(False, False)
        n.down = node
        node.up = addNode(n, currentXIndex, currentYIndex - 1)
    else:
        return -1

    return node