from django.test import TestCase
from django.utils import timezone
from hello.models import LogMessage
import datetime

class LogMessageModelTest(TestCase):

    def create_logmessage(self, message="This is a test message"):
        """
        Create and return a LogMessage instance
        """
        return LogMessage.objects.create(
            message=message,
            log_data=timezone.now()
        )

    def test_logmessage_creation(self):
        """
        Test the creation of a log message instance
        """
        log_message = self.create_logmessage()
        self.assertTrue(isinstance(log_message, LogMessage.model))

