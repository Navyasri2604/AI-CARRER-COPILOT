from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from accounts.models import UserProfile
from .models import Roadmap, RoadmapTask

class RoadmapPermissionTests(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user('owner', password='StrongPass123!')
        self.other = User.objects.create_user('other', password='StrongPass123!')
        UserProfile.objects.create(user=self.owner)
        UserProfile.objects.create(user=self.other)
        roadmap = Roadmap.objects.create(user=self.owner, role='Software Engineer')
        self.task = RoadmapTask.objects.create(roadmap=roadmap, title='Learn testing')

    def test_user_cannot_toggle_another_users_task(self):
        self.client.force_login(self.other)
        response = self.client.post(reverse('toggle-roadmap-task', args=[self.task.id]))
        self.assertEqual(response.status_code, 404)
        self.task.refresh_from_db()
        self.assertFalse(self.task.completed)
