from node import Node
from random import getrandbits

# if current index < max index than
# set my right node
# link my current
# set my down node


def linkNodes(node, maxIndx, currIndx):
    if currIndx <= maxIndx:
        node.setRight(linkNodes(Node(getrandbits(1), False), maxIndx, currIndx + 1))
        node.setDown(linkNodes(Node(getrandbits(1), False), maxIndx, currIndx + 1))
    return node

def setFinishNode(node, xIndex, yIndex):
    for i in range(0, xIndex):
        node = node.right
    for i in range(0, yIndex):
        node = node.down
    node.isFinish = True
    return node