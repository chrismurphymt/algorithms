class DisjointSet():
    def __init__(self, val):
        self.value = val
        self.parent = self

        self.rank = 1
