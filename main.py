if __name__ == "__main__":
    from node import Node
    from random import getrandbits
    from traversal import traverse

    rootNode = Node(False, False)

    n = rootNode
    for i in range(0, 5):
        n.setRight(Node(getrandbits(1), False))
        n.setDown(Node(getrandbits(1), False))

        nn = n.down
        n = n.right

        for a in range(0, 5):
            nn.setDown(Node(False, False))
            nn = nn.down
            if i == 4 and a == 4:
                nn.isFinish = True

    a = traverse(rootNode.down.down.down.down.down)
    print(a)