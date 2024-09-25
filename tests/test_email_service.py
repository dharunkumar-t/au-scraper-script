import unittest
from unittest.mock import patch
from email_service import send_email

class TestEmailService(unittest.TestCase):

    @patch('email_service.smtplib.SMTP')
    def test_send_email_valid(self, mock_smtp):
        mock_instance = mock_smtp.return_value
        mock_instance.sendmail.return_value = True
        result = send_email("Test Subject", "Test message", "recipient@example.com")
        self.assertTrue(result)

    @patch('email_service.smtplib.SMTP')
    def test_send_email_invalid_recipient(self, mock_smtp):
        mock_instance = mock_smtp.return_value
        mock_instance.sendmail.side_effect = Exception("Invalid email address")
        with self.assertRaises(Exception) as context:
            send_email("Test Subject", "Test message", "invalid_email")
        self.assertEqual(str(context.exception), "Invalid email address")

    def test_send_email_no_subject(self):
        with self.assertRaises(ValueError):
            send_email("", "Test message", "recipient@example.com")

    def test_send_email_no_message(self):
        with self.assertRaises(ValueError):
            send_email("Test Subject", "", "recipient@example.com")

if __name__ == '__main__':
    unittest.main()
