from django.test import SimpleTestCase
import requests
from django.conf import settings


class TestFlaskRequest(SimpleTestCase):
    def test_status_check(self):
        url = f"{settings.HEALTH_CHECKER_URL}1/"
        request = requests.get(url)
        self.assertIn(request.status_code, [200, 503])
