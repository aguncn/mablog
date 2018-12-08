from django.test import TestCase
from model_mommy import mommy
from wslog.models import LogsDB


class MabLogModelTestMommy(TestCase):
    def test_app_creation_mommy(self):
        new_log = mommy.make(LogsDB)
        self.assertTrue(isinstance(new_log, LogsDB))
        self.assertEqual(new_log.__str__(), new_log.add_date)
