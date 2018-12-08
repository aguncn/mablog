from django.test import TestCase
from django.urls import resolve, reverse
from wslog.views import log_add, log_show

'''
headers = {'Content-Type': 'application/json;charset=utf-8'}
payload = {'deploy_version': "2018-06-21-12DB",
           'app_name': "ZIP-BACKEND-JAVA",
           'ip_address': "1.1.1.1",
           'env_name': "UAT",
           'user_name': "sky",
           'operation_type': "deploy",
           'operation_no': 8,
           'log_content': "...2018-07-23 08:43:38deploypkg \
           cnsz141851-10.25.164.108, deploy progress 80%"}
'''


class MabLogCreateTests(TestCase):

    def test_log_add_view_status_code(self):
        url = reverse('log_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_log_add_url_resolves_view(self):
        view = resolve('/wslog/log_add/')
        self.assertEqual(view.func.__name__, log_add.__name__)


class MabLogShowTests(TestCase):

    def test_log_show_view_status_code(self):
        url = reverse('log_show')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_log_show_url_resolves_view(self):
        view = resolve('/wslog/log_show/')
        self.assertEqual(view.func.__name__, log_show.__name__)
