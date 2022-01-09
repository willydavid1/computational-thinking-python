import unittest

def is_older(age):
    if age >= 18:
        return True
    else:
        return False

class Glass_Box_Testing(unittest.TestCase):
    def test_is_older(self):
        age = 20
        result = is_older(age)

        self.assertEqual(result, True)

    def test_minor_child(self):
        age = 15
        result = is_older(age)

        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main()