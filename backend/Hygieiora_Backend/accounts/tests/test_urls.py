from django.urls import reverse
from rest_framework.test import APITestCase
from accounts.views import *
import uuid


class AccountsUrlsTestCase(APITestCase):
    def test_user_list_url_resolves(self):
        view_name = "user-list"
        expected_url = reverse(view_name)

        self.assertEquals(expected_url, "/accounts/users/")

    def test_register_user_url_resolves(self):
        view_name = "auth-register"
        expected_url = reverse(view_name)

        self.assertEquals(expected_url, "/accounts/register/")

    def test_login_user_url_resolves(self):
        view_name = "token_obtain_pair"
        expected_url = reverse(view_name)

        self.assertEquals(expected_url, "/accounts/login/")


class UUIDViewTestCase(APITestCase):
    test_uuid = uuid.uuid4()

    def test_user_detail_url_resolves(self):
        view_name = "user-detail"
        expected_url = reverse(view_name, args=[self.test_uuid])

        self.assertEquals(expected_url, f"/accounts/users/{self.test_uuid}/")
