from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from authentication.views import RegisterView


class RegisterViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('register')
        self.user_data = {
            'username': 'testuser',
            'email': 'testsuer@gmail.com',
            'password': 'testpassword',
            'first_name': 'test',
            'last_name': 'user'
        }

    def test_register_view_should_create_user_object(self):
        response = self.client.post(self.url, self.user_data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_view_should_not_create_user_with_same_payload(self):
        first_response = self.client.post(self.url, self.user_data)
        second_response = self.client.post(self.url, self.user_data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(first_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(second_response.status_code,
                         status.HTTP_400_BAD_REQUEST)
