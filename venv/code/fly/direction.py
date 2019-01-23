class Direction(object):
    '''
      方向类，用来描述当前飞机的方向
    '''
    def __init__(self):
        self.left = False
        self.right = False
        self.up = False
        self.down = False

    def setleft(self, bool):
        self.left = bool

    def setright(self, bool):
        self.right = bool

    def setup(self, bool):
        self.up = bool

    def setdown(self, bool):
        self.down = bool

    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def getup(self):
        return self.up

    def getdown(self):
        return self.down