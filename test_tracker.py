import unittest
import tracker

class TestTracker(unittest.TestCase):
    def test_percentage(self):
        self.assertEqual(tracker.get_percentage(8, 10), 80.0)
        self.assertEqual(tracker.get_percentage(0, 0), 0.0)

    def test_bunks(self):
        # 10 attended out of 10 held -> safe to bunk 3 classes (10/13 = 76.9%)
        self.assertEqual(tracker.calculate_safe_bunks(10, 10), 3)

    def test_recovery(self):
        # 5 attended out of 10 held (50%) -> needs 10 consecutive classes to reach 75%
        self.assertEqual(tracker.calculate_needed_classes(5, 10), 10)

if __name__ == "__main__":
    unittest.main()