from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from authentication.views import LoginView


class LoginViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('login')
        self.user = User.objects.create_user(username='test', password='test')
        self.user.save()
        self.data = {'username': 'test', 'password': 'test'}

    def test_login_view(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_view_with_invalid_data(self):
        self.data['password'] = 'invalid'
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
