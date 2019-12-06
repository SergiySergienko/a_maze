class Node(object):
    """docstring"""

    def __init__(self, isWall, isFinish):
        """Constructor"""
        self.value = 0
        self.isWall = isWall
        self.isFinish = isFinish
        self.up = None
        self.right = None
        self.down = None
        self.left = None
        self.currentState = ""

    def setRight(self, node):
        self.right = node
        node.left = self

    def setLeft(self, node):
        self.left = node
        node.right = self

    def setUp(self, node):
        self.up = node
        node.down = self

    def setDown(self, node):
        self.down = node
        node.up = self

    def setState(self, state):
        self.currentState = state

    def getState(self):
        return self.currentState