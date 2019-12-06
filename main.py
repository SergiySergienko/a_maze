if __name__ == "__main__":
    from node import Node
    from field_builder import *
    from traversal import traverse

    rootNode = Node(False, False)
    linkNodes(rootNode, 5, 0)
    setFinishNode(rootNode, 4, 4)

    print(rootNode)
