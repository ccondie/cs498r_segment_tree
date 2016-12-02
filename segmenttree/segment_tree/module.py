import math
import sys


class SegmentTree(object):
    def __init__(self, size):
        self.size = size
        self.tree_nodes = (2 ** (math.ceil(math.log(size, 2)) + 1)) - 1
        self.tree = [0] * self.tree_nodes
        self.max_leaf = 2 ** (math.ceil(math.log(size, 2)))

    def setValue(self, value, index):
        # change the value at the index
        tree_index = self.get_tree_index(index)
        self.tree[tree_index] = value

        # until we get to the root node
        while tree_index != 0:
            # get the parent of that node
            tree_index = self.parentIndex(tree_index)
            # update it to the sum of its children
            self.tree[tree_index] = self.tree[self.childLeftIndex(tree_index)] + self.tree[
                self.childRightIndex(tree_index)]

    def getSum(self, indexLeft, indexRight):
        cur_index = 0
        int_low = 0
        int_high = self.size - 1

        return self.getSumNode(indexLeft, indexRight, cur_index, int_low, int_high)

    def getSumNode(self, indexLeft, indexRight, tree_index, int_low, int_high):
        # if there is no overlap
        if int_high < indexLeft or int_low > indexRight:
            return 0

        # if the interval of the current node is inside (inclusively) the range we are looking for, then we return the value of the node
        if int_high <= indexRight and int_low >= indexLeft:
            return self.tree[tree_index]

        # fallback case: If any part of the interval of the node we are currently at is outside the range we are searching for, we call this function on its two children.
        int_len = int_high - int_low
        mid_index_mod = math.floor(int_len / 2)

        childLeft = self.childLeftIndex(tree_index)
        childRight = self.childRightIndex(tree_index)

        leftVal = self.getSumNode(indexLeft, indexRight, childLeft, int_low, int_low + mid_index_mod)
        rightVal = self.getSumNode(indexLeft, indexRight, childRight, int_low + mid_index_mod + 1, int_high)

        return leftVal + rightVal

    def get_tree_index(self, default_index):
        cur_index = 0
        int_low = 0
        int_high = self.size - 1
        int_len = int_high - int_low

        while int_len != 0:
            # get the size of the interval represented at cur_index
            mid_index_mod = math.floor(int_len / 2)
            if default_index <= int_low + mid_index_mod:
                # if the index we are searching for falls to the left of the interval split
                cur_index = self.childLeftIndex(cur_index)
                int_low = int_low
                int_high = int_low + mid_index_mod
            else:
                # if the index we are searching for falls to the right on the interval split
                cur_index = self.childRightIndex(cur_index)
                int_low = int_low + mid_index_mod + 1
                int_high = int_high
            int_len = int_high - int_low
        return cur_index

    def childLeftIndex(self, parentIndex):
        return parentIndex * 2 + 1

    def childRightIndex(self, parentIndex):
        return parentIndex * 2 + 2

    def parentIndex(self, childIndex):
        return math.floor((childIndex - 1) / 2)


class SegmentTreeMax(object):
    def __init__(self, size):
        self.size = size
        self.tree_nodes = (2 ** (math.ceil(math.log(size, 2)) + 1)) - 1
        self.tree = [0] * self.tree_nodes
        self.max_leaf = 2 ** (math.ceil(math.log(size, 2)))

    def setValue(self, value, index):
        # change the value at the index
        tree_index = self.get_tree_index(index)
        self.tree[tree_index] = value

        # until we get to the root node
        while tree_index != 0:
            # get the parent of that node
            tree_index = self.parentIndex(tree_index)
            # update it to the sum of its children
            self.tree[tree_index] = self.tree[self.childLeftIndex(tree_index)] + self.tree[
                self.childRightIndex(tree_index)]

    def getMax(self, indexLeft, indexRight):
        maxVal = -sys.maxsize
        for index in range(indexLeft, indexRight + 1):
            index = self.get_tree_index(index)
            if self.tree[index] > maxVal:
                maxVal = self.tree[index]
        return maxVal

    def get_tree_index(self, default_index):
        cur_index = 0
        int_low = 0
        int_high = self.size - 1
        int_len = int_high - int_low

        while int_len != 0:
            # get the size of the interval represented at cur_index
            mid_index_mod = math.floor(int_len / 2)
            if default_index <= int_low + mid_index_mod:
                # if the index we are searching for falls to the left of the interval split
                cur_index = self.childLeftIndex(cur_index)
                int_low = int_low
                int_high = int_low + mid_index_mod
            else:
                # if the index we are searching for falls to the right on the interval split
                cur_index = self.childRightIndex(cur_index)
                int_low = int_low + mid_index_mod + 1
                int_high = int_high
            int_len = int_high - int_low
        return cur_index

    def childLeftIndex(self, parentIndex):
        return parentIndex * 2 + 1

    def childRightIndex(self, parentIndex):
        return parentIndex * 2 + 2

    def parentIndex(self, childIndex):
        return math.floor((childIndex - 1) / 2)


class SegmentTreeScheduler(object):
    """
    The nature of this segment tree will be that each leaf node will represent a minute in the day (for simplicity's sake there will be minutes 61-999)
    contained in each leaf node will be a representation of the number of meetings scheduled for that minute
    """
    def __init__(self, size):
        self.size = size
        self.tree_nodes = (2 ** (math.ceil(math.log(size, 2)) + 1)) - 1
        self.tree = [0] * self.tree_nodes
        self.max_leaf = 2 ** (math.ceil(math.log(size, 2)))

    def setMeeting(self, startTime, endTime):
        """
        works by incrementing the number of meetings in each minute from startTime to endTime
        :param startTime:
        :param endTime:
        :return:
        """
        for index in range(startTime, endTime + 1):
            self.tree[self.get_tree_index(index)] += 1

    def numberOfMeetingsTakingPlace(self, time):
        """
        the way the tree is build getting the number of meetings at any given time is as simple as a lookup
        :param time:
        :return:
        """
        return self.tree[self.get_tree_index(time)]

    def roomsOccupied(self, startTime, endTime):
        """
        this method looks for the greatest number of meetings (biggest leaf node) in the given time range
        :param startTime:
        :param endTime:
        :return:
        """
        maxVal = -sys.maxsize
        for index in range(startTime, endTime + 1):
            index = self.get_tree_index(index)
            if self.tree[index] > maxVal:
                maxVal = self.tree[index]
        return maxVal

    def setValue(self, value, index):
        # change the value at the index
        tree_index = self.get_tree_index(index)
        self.tree[tree_index] = value

        # until we get to the root node
        while tree_index != 0:
            # get the parent of that node
            tree_index = self.parentIndex(tree_index)
            # update it to the sum of its children
            self.tree[tree_index] = self.tree[self.childLeftIndex(tree_index)] + self.tree[
                self.childRightIndex(tree_index)]

    def get_tree_index(self, default_index):
        cur_index = 0
        int_low = 0
        int_high = self.size - 1
        int_len = int_high - int_low

        while int_len != 0:
            # get the size of the interval represented at cur_index
            mid_index_mod = math.floor(int_len / 2)
            if default_index <= int_low + mid_index_mod:
                # if the index we are searching for falls to the left of the interval split
                cur_index = self.childLeftIndex(cur_index)
                int_low = int_low
                int_high = int_low + mid_index_mod
            else:
                # if the index we are searching for falls to the right on the interval split
                cur_index = self.childRightIndex(cur_index)
                int_low = int_low + mid_index_mod + 1
                int_high = int_high
            int_len = int_high - int_low
        return cur_index

    def childLeftIndex(self, parentIndex):
        return parentIndex * 2 + 1

    def childRightIndex(self, parentIndex):
        return parentIndex * 2 + 2

    def parentIndex(self, childIndex):
        return math.floor((childIndex - 1) / 2)
