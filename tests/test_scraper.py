import unittest
from unittest.mock import patch
from scraper import get_announcements

class TestScraper(unittest.TestCase):

    @patch('scraper.webdriver.Chrome')
    def test_get_announcements_valid_page(self, mock_chrome):
        mock_driver = mock_chrome.return_value
        mock_driver.find_elements.return_value = [
            mock_driver,  # Mocked element
            mock_driver   # Another mocked element
        ]
        mock_driver.text = "Announcement 1"
        announcements = get_announcements()
        self.assertIsInstance(announcements, list)
        self.assertGreater(len(announcements), 0)
        self.assertIn("Announcement 1", announcements)

    @patch('scraper.webdriver.Chrome')
    def test_get_announcements_no_elements(self, mock_chrome):
        mock_driver = mock_chrome.return_value
        mock_driver.find_elements.return_value = []

        announcements = get_announcements()
        self.assertEqual(announcements, [])

    @patch('scraper.webdriver.Chrome')
    def test_get_announcements_timeout(self, mock_chrome):
        mock_driver = mock_chrome.return_value
        mock_driver.get.side_effect = Exception("Timeout")
        with self.assertRaises(Exception):
            get_announcements()

if __name__ == '__main__':
    unittest.main()
