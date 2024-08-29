import unittest
import pandas as pd
from src.loader import load_news_data

class TestLoader(unittest.TestCase):
    def test_load_news_data(self):
        test_file_path = '../data/rating.csv'
        data = load_news_data(test_file_path)
        self.assertIsInstance(data, pd.DataFrame)
        self.assertFalse(data.empty)

        expected_columns = ['article_id', 'source_name', 'title', 'content', 'published_at', 'title_sentiment']
        for col in expected_columns:
            self.assertIn(col, data.columns)

        self.assertTrue(pd.api.types.is_datetime64_any_dtype(data['published_at']))
        self.assertTrue(pd.api.types.is_categorical_dtype(data['title_sentiment']))

if __name__ == '__main__':
    unittest.main()
