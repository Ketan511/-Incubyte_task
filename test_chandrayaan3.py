import unittest
from chandrayaan3 import Chandrayaan3 

class TestChandrayaan3(unittest.TestCase):
    # Existing test

    def test_move_forward(self):
        chandrayaan = Chandrayaan3()
        chandrayaan.move('f')
        self.assertEqual(chandrayaan.getPosition(), [0, 1, 0])

    def test_move_backward(self):
        chandrayaan = Chandrayaan3()
        chandrayaan.move('b')
        self.assertEqual(chandrayaan.getPosition(), [0, -1, 0])

    def test_turn_left(self):
        chandrayaan = Chandrayaan3()
        chandrayaan.turn('l')
        self.assertEqual(chandrayaan.getDirection(), 'W')

    def test_turn_right(self):
        chandrayaan = Chandrayaan3()
        chandrayaan.turn('r')
        self.assertEqual(chandrayaan.getDirection(), 'E')

    def test_tilt_up(self):
        chandrayaan = Chandrayaan3()
        chandrayaan.tilt('u')
        self.assertEqual(chandrayaan.getDirection(), 'U')

    def test_tilt_down(self):
        chandrayaan = Chandrayaan3()
        chandrayaan.tilt('d')
        self.assertEqual(chandrayaan.getDirection(), 'D')