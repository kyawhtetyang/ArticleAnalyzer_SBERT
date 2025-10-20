import sys, os
# Add parent folder to sys.path first
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from src.pipeline import full_pipeline
import json

class TestPipeline(unittest.TestCase):
    def test_full_pipeline(self):
        with open("data/config.json") as f:
            config = json.load(f)
        df, recs = full_pipeline(config)
        self.assertTrue('sentiment' in df.columns)
        self.assertTrue('summary' in df.columns)
        self.assertTrue(isinstance(recs, dict))

if __name__ == "__main__":
    unittest.main()

