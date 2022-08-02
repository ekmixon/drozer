import unittest

from mwr.cinnibar import reflection
from mwr.cinnibar.api.protobuf_pb2 import Message

from mwr_test.mocks.reflection import MockReflector

class ReflectedNullTestCase(unittest.TestCase):

    def setUp(self):
        pass

def ReflectedNullTestSuite():
    #suite.addTest(ReflectedNullTestCase("testItShouldGetAPropertyValue"))

    return unittest.TestSuite()
  
if __name__ == "__main__":
    unittest.TextTestRunner().run(ReflectedNullTestSuite())
    