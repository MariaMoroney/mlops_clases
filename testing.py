import unittest
from suma import suma

class TestSuma(unittest.TestCase):
    def test_suma(self):
        resultado_suma = suma(2,3)
        self.assertEqual(suma(2,3),8)



if __name__ == '__main__':
    unittest.main()
