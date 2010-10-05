import unittest

from return_optimiser import *

class FindingReturns(unittest.TestCase):

    def test_one_uptick(self):
        ticks = [(50.0, 'b')]
        best = find_best_return(ticks, 'a')
        self.assertAlmostEqual(best.roi, 1.5)
        self.assertEqual(best.low_date, 'a')
        self.assertEqual(best.high_date, 'b')

    def test_one_downtick(self):
        ticks = [(-50.0, 'b')]
        best = find_best_return(ticks, 'a')
        self.assertAlmostEqual(best.roi, 1.0)
        self.assertEqual(best.low_date, 'a')
        self.assertEqual(best.high_date, 'a')

    def test_two_upticks(self):
        ticks = [(10.0, 'b'),
                 (10.0, 'c')]
        best = find_best_return(ticks, 'a')
        self.assertAlmostEqual(best.roi, 1.21)
        self.assertEqual(best.low_date, 'a')
        self.assertEqual(best.high_date, 'c')

    def test_false_first_maximum(self):
        ticks = [( 10.0, 'b'),
                 (-10.0, 'c'),
                 ( 10.0, 'd'),
                 ( 10.0, 'e')]
        best = find_best_return(ticks, 'a')
        self.assertAlmostEqual(best.roi, 1.21)
        self.assertEqual(best.low_date, 'c')
        self.assertEqual(best.high_date, 'e')

    def test_lesser_second(self):
        ticks = [( 50.0, 'b'),
                 (-50.0, 'c'),
                 ( 10.0, 'd'),
                 ( 10.0, 'e')]
        best = find_best_return(ticks, 'a')
        self.assertAlmostEqual(best.roi, 1.5)
        self.assertEqual(best.low_date, 'a')
        self.assertEqual(best.high_date, 'b')

    def test_find_tight_range(self):
        ticks = [( 0.0, 'b'),
                 ( 0.0, 'c'),
                 (50.0, 'd'),
                 ( 0.0, 'e'),
                 ( 0.0, 'f')]
        best = find_best_return(ticks, 'a')
        self.assertAlmostEqual(best.roi, 1.5)
        self.assertEqual(best.low_date, 'c')
        self.assertEqual(best.high_date, 'd')

    def test_not_enough_ticks(self):
        ticks = []
        best = find_best_return(ticks, 'a')
        self.assertEqual(best.low_date, 'a')
        self.assertEqual(best.high_date, 'a')

    def test_given_sample(self):
        ticks = [(-8.00, '09/10/06'),
                 (10.00, '10/10/06'),
                 (-5.00, '11/10/06'),
                 ( 7.00, '12/10/06'),
                 (-2.00, '13/10/06')]
        best = find_best_return(ticks, '06/10/06')
        self.assertAlmostEqual(best.roi, 1.118, places=3)
        self.assertEqual(best.low_date, '09/10/06')
        self.assertEqual(best.high_date, '12/10/06')

if __name__=='__main__':
    unittest.main()
