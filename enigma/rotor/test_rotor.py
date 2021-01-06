import unittest
import rotor

class TestRotor(unittest.TestCase):
    """TestRotor ...
    """

    def test_init(self):
        tt = [
            {"num" : 1, "expected" : "EKMFLGDQVZNTOWYHXUSPAIBRCJ"},
            {"num" : 2, "expected" : "AJDKSIRUXBLHWTMCQGZNPYFVOE"},
            {"num" : 3, "expected" : "BDFHJLCPRTXVZNYEIWGAKMUSQO"},            
        ]
        for tc in tt:
            rtor = rotor.Rotor(tc["num"])
            self.assertEqual(tc["expected"], rtor.sub)
