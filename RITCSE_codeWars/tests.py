from django.test import TestCase

# Create your tests here.
from django.utils.datetime_safe import datetime

from RITCSE_codeWars.models import Contest


class TestAllSubmissions(TestCase):
    def test_rank_list_formation(self):
        contest = Contest(name="test",contest_start_date=datetime.now()-,
                          contest_end_date=)