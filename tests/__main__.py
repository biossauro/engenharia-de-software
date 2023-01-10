import unittest
import xmlrunner
from tests.test_stack import TestStack

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="reports"),
                  failfast=False, buffer=False, catchbreak=False, exit=False)
