# 0 1 2 3
# 1 1 2 3
# 2 2 3 4
# 3 4 1 4

def traverse(node):
    print(node)
    doTraverse(node, node)


def doTraverse(fromNode, toNode):
    print(fromNode, toNode)

    if toNode != None and toNode.isFinish == True:
        return 1

    if fromNode.getState() == "up":
        if fromNode.right != None and fromNode.right.isWall == False:
            fromNode.setState("right")
            return doTraverse(fromNode, fromNode.right)
    elif fromNode.getState() == "right":
        if fromNode.down != None and fromNode.down.isWall == False:
            fromNode.setState("down")
            return doTraverse(fromNode, fromNode.down)
    elif fromNode.getState() == "down":
        if fromNode.left != None and fromNode.left.isWall == False:
            fromNode.setState("left")
            return doTraverse(fromNode, fromNode.left)
    elif fromNode.getState() == "left":
        return doTraverse(toNode, fromNode)
    else:
        if fromNode.up != None and fromNode.up.isWall == False:
            fromNode.setState("up")
            return doTraverse(fromNode, fromNode.up)
        else:
            return -1