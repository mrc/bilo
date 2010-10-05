import unittest

from bilo import *

class PriceGenerator(unittest.TestCase):

    def test_price_generator(self):
        ticks = [1, 0.92, 1.1, 0.95, 1.07, 0.98, 0.5, 0.6, 3.0]

        prices = [p for p in price_generator(ticks)]
        expected_prices = [1.0, 0.92, 1.012, 0.961, 1.029, 1.008]
        for p, e in zip(prices, expected_prices):
            self.assertAlmostEqual(p, e, places=3)

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
