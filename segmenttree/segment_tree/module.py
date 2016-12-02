import math


class SegmentTree(object):
    def __init__(self, size):
        self.size = size
        self.tree_size = (2 ** (math.ceil(math.log(size, 2)) + 1)) - 1
        self.tree = [0] * self.tree_size

    def setValue(self, value, index):
        # change the value at the index
        self.tree[index] = value

        # until we get to the root node
        while index != 0:
            # get the parent of that node
            index = self.parentIndex(index)
            # update it to the sum of its children
            self.tree[index] = self.tree[self.childLeftIndex(index)] + self.tree[self.childRightIndex(index)]

    def getSum(self, indexLeft, indexRight):
        pass

    def get_tree_index(self, default_index):
        int_low = 0
        int_high = self.size - 1
        while int_high - int_low != 0:
            pass

    def childLeftIndex(self, parentIndex):
        return parentIndex * 2 + 1

    def childRightIndex(self, parentIndex):
        return parentIndex * 2 + 2

    def parentIndex(self, childIndex):
        return math.floor((childIndex - 1) / 2)


class SegmentTreeMax(object):
    def __init__(self, size):
        self.size = size

    def setValue(self, value, index):
        pass

    def getMax(self, indexLeft, indexRight):
        pass


class SegmentTreeScheduler(object):
    def __init__(self, size):
        self.size = size

    def setMeeting(self, startTime, endTime):
        pass

    def numberOfMeetingsTakingPlace(self, time):
        pass

    def roomsOccupied(selfself, startTime, endTime):
        pass
