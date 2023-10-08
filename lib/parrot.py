import io
import sys
import unittest

def parrot(argument="Squawk!"):
    print(argument)
    return argument

class TestParrot(unittest.TestCase):
    def test_prints_argument(self):
        '''prints the argument passed to it.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        result = parrot("Hello!")  # Call parrot with an argument
        sys.stdout = sys.__stdout__  # Restore sys.stdout
        self.assertEqual(captured_out.getvalue(), "Hello!\n")
        self.assertEqual(result, "Hello!")

if __name__ == '__main__':
    unittest.main()
