from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import UserProfile

class AccountFlowTests(TestCase):
    def test_registration_creates_profile_and_logs_user_in(self):
        response = self.client.post(reverse('register'), {'username': 'new_user', 'email': 'new@example.com', 'password1': 'StrongPass123!', 'password2': 'StrongPass123!'})
        self.assertRedirects(response, reverse('dashboard'))
        self.assertTrue(UserProfile.objects.filter(user__username='new_user').exists())

    def test_logout_link_clears_session(self):
        user = User.objects.create_user('logout_user', password='StrongPass123!')
        self.client.force_login(user)
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('home'))
        self.assertNotIn('_auth_user_id', self.client.session)
