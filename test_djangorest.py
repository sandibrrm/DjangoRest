# test_djangorest.py
"""
Tests for DjangoRest module.
"""

import unittest
from djangorest import DjangoRest

class TestDjangoRest(unittest.TestCase):
    """Test cases for DjangoRest class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DjangoRest()
        self.assertIsInstance(instance, DjangoRest)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DjangoRest()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
