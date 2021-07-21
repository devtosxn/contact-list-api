from django.test import TestCase
from django.contrib.auth.models import User
from contacts.models import Contacts


class TestContactsModel(TestCase):
    """Contact model tests."""

    def setUp(self):
        self.contact = Contacts.objects.create(
            first_name="John",
            last_name="Doe",
            email="jdoe@gmail.com",
            phone_number="1234567890",
            avatar="http://www.google.com/image.png",
            is_favorite=False,
            country_code="123",
            owner=User.objects.create_user(
                username="jdoe", password="password")
        )
        self.contact.save()

    def test_contact_creation(self):
        """
        Test that contact is created
        """
        self.assertTrue(Contacts.objects.exists())

    def test_contact_string_representation(self):
        """
        Test that contact is represented by its first name
        """
        self.assertEqual(str(self.contact), "John Doe")
