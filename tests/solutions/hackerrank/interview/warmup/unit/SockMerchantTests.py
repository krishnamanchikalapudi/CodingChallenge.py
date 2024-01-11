import time, unittest
from scripts.solutions.hackerrank.interview.warmup.SockMerchant import SockMerchant as SockMerchant

class SockMerchantTests(unittest.TestCase):
    tests= SockMerchant()

    def test1(self):
        input = [1, 2, 1, 2, 1, 3, 2]
        expected = 2
        actual = self.tests.solution(input)
        print(f"Actual: {actual}, Expect: {expected}")
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(SockMerchantTests)
    unittest.TextTestRunner(verbosity=0).run(suite)