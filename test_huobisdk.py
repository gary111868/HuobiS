# test_huobisdk.py
"""
Tests for HuobiSDK module.
"""

import unittest
from huobisdk import HuobiSDK

class TestHuobiSDK(unittest.TestCase):
    """Test cases for HuobiSDK class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HuobiSDK()
        self.assertIsInstance(instance, HuobiSDK)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HuobiSDK()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
