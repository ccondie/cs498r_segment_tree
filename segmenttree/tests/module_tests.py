''' You will need the following import if using python2 '''
from __future__ import absolute_import

from ..segment_tree.module import *
import unittest


class SegmentTree_Test(unittest.TestCase):
    """This is an example of a Testing class. You'll want to replace this comment with your own.
    """

    def setUp(self):
        self.def_seg = SegmentTree(8)
        self.def_seg.setValue(5, 0)
        self.def_seg.setValue(3, 1)
        self.def_seg.setValue(2, 2)
        self.def_seg.setValue(5, 3)
        self.def_seg.setValue(7, 4)
        self.def_seg.setValue(2, 5)
        self.def_seg.setValue(1, 6)
        self.def_seg.setValue(9, 7)

        self.def_seg_max = SegmentTreeMax(8)
        self.def_seg_max.setValue(5, 0)
        self.def_seg_max.setValue(3, 1)
        self.def_seg_max.setValue(2, 2)
        self.def_seg_max.setValue(5, 3)
        self.def_seg_max.setValue(7, 4)
        self.def_seg_max.setValue(2, 5)
        self.def_seg_max.setValue(1, 6)
        self.def_seg_max.setValue(9, 7)

        self.def_seg_sched = SegmentTreeScheduler(2400)

    def test_size(self):
        """Test that the size attribute exists
        """
        seg = SegmentTree(10)
        self.assertEqual(hasattr(seg, "size"), True)

        segMax = SegmentTreeMax(10)
        self.assertEqual(hasattr(segMax, "size"), True)

        segSched = SegmentTreeScheduler(10)
        self.assertEqual(hasattr(segSched, "size"), True)

    '''
    MISC TESTS
    '''

    def test_single_setValue(self):
        seg = SegmentTree(10)
        seg.setValue(10, 5)
        self.assertEqual(seg.tree[0], seg.tree[5])

    def test_get_tree_index(self):
        seg = SegmentTree(8)
        self.assertEqual(seg.get_tree_index(3), 10)
        self.assertEqual(seg.get_tree_index(0), 7)
        self.assertEqual(seg.get_tree_index(7), 14)

    def test_double_setValue(self):
        print(self.def_seg.tree)

    def test_get_sum(self):
        print(self.def_seg.getSum(2, 6))
        self.assertEqual(self.def_seg.getSum(2, 6), 17)
        print(self.def_seg.getSum(3, 3))
        self.assertEqual(self.def_seg.getSum(3, 3), 5)
        
    def test_get_max(self):
        print(self.def_seg_max.getMax(0,7))
        self.assertEqual(self.def_seg_max.getMax(0,7), 9)
        print(self.def_seg_max.getMax(1,3))
        self.assertEqual(self.def_seg_max.getMax(1,3), 5)

    def test_num_meeting(self):
        self.def_seg_sched.setMeeting(800, 1000)
        print(self.def_seg_sched.numberOfMeetingsTakingPlace(900))
        self.assertEqual(self.def_seg_sched.numberOfMeetingsTakingPlace(900), 1)
        self.def_seg_sched.setMeeting(900, 1100)
        print(self.def_seg_sched.numberOfMeetingsTakingPlace(900))
        self.assertEqual(self.def_seg_sched.numberOfMeetingsTakingPlace(900), 2)
        self.def_seg_sched.setMeeting(1010,1020)
        print(self.def_seg_sched.numberOfMeetingsTakingPlace(925))
        self.assertEqual(self.def_seg_sched.numberOfMeetingsTakingPlace(925), 2)

    def test_max_rooms(self):
        self.def_seg_sched.setMeeting(800, 1000)
        print(self.def_seg_sched.numberOfMeetingsTakingPlace(900))
        self.assertEqual(self.def_seg_sched.numberOfMeetingsTakingPlace(900), 1)
        self.def_seg_sched.setMeeting(900, 1100)
        print(self.def_seg_sched.numberOfMeetingsTakingPlace(900))
        self.assertEqual(self.def_seg_sched.numberOfMeetingsTakingPlace(900), 2)
        self.def_seg_sched.setMeeting(1010, 1020)
        print(self.def_seg_sched.numberOfMeetingsTakingPlace(925))
        self.assertEqual(self.def_seg_sched.numberOfMeetingsTakingPlace(925), 2)
        print(self.def_seg_sched.roomsOccupied(800,1100))
        self.assertEqual(self.def_seg_sched.roomsOccupied(800,1100), 2)

