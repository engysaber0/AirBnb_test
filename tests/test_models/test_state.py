#!/usr/bin/python3
"""second class"""
"""let's test state class"""
import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
 
    def test_state(self):
	"""عملت ل id, created, updated  عش�ان �ورثتهم من ال لاشسث_ةخيثم"""
        """let's check attributes of state"""
        st = State()
        self.assertTrue(hasattr(st, "id"))
        self.assertIsInstance(st.id, str)
        self.assertTrue(hasattr(st, "created_at"))
        self.assertIsInstance(st.created_at, datetime)
        self.assertTrue(hasattr(st, "updated_at"))
        self.assertIsInstance(st.updated_at, datetime)
        self.assertTrue(hasattr(st, "name"))
        self.assertIsInstance(st.name, str)


if __name__ == "__main__":
    unittest.main()
