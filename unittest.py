import unittest
from task import fib

class TestWorker(unittest.TestCase):
    def test_fib(self):
	self.assertEqual(fib(-1), [])
	self.assertEqual(fib(1), [0,1])
	self.assertEqual(fib(2), [0,1,1])
	self.assertEqual(fib(3), [0,1,1,2])

def main():
    unittest.main()

if __name__ == '__main__':
    main()
