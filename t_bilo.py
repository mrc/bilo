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
        ticks = [(1, 'a'), (1.5, 'b')]
        best = find_best_return(ticks, 'start')
        self.assertAlmostEqual(best.roi, 1.5)
        self.assertEqual(best.low_date, 'a')
        self.assertEqual(best.high_date, 'b')

    def test_one_downtick(self):
        ticks = [(1, 'a'), (0.5, 'b')]
        best = find_best_return(ticks, 'start')
        self.assertAlmostEqual(best.roi, 1.0)
        self.assertEqual(best.low_date, 'start')
        self.assertEqual(best.high_date, 'start')

    def test_two_upticks(self):
        ticks = [(1,   'a'),
                 (1.1, 'b'),
                 (1.1, 'c')]
        best = find_best_return(ticks, 'start')
        self.assertAlmostEqual(best.roi, 1.21)

    def test_false_first_maximum(self):
        ticks = [(1,   'a'),
                 (1.1, 'b'),
                 (0.9, 'c'),
                 (1.1, 'd'),
                 (1.1, 'e')]
        best = find_best_return(ticks, 'start')
        self.assertAlmostEqual(best.roi, 1.21)
        self.assertEqual(best.low_date, 'c')
        self.assertEqual(best.high_date, 'e')

    def test_lesser_second(self):
        ticks = [(1,   'a'),
                 (1.5, 'b'),
                 (0.5, 'c'),
                 (1.1, 'd'),
                 (1.1, 'e')]
        best = find_best_return(ticks, 'start')
        self.assertAlmostEqual(best.roi, 1.5)

    def test_given_sample(self):
        ticks = [(0.92, '09/10/06'),
                 (1.1,  '10/10/06'),
                 (0.95, '11/10/06'),
                 (1.07, '12/10/06'),
                 (0.98, '13/10/06')]
        best = find_best_return(ticks, '06/10/06')
        self.assertAlmostEqual(best.roi, 1.118, places=3)
        self.assertEqual(best.low_date, '09/10/06')
        self.assertEqual(best.high_date, '12/10/06')

if __name__=='__main__':
    unittest.main()
