from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from accounts.models import UserProfile
from resume_analysis.models import ResumeAnalysis
from .models import JobApplication, JobMatch

class CareerToolsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('career_user', password='StrongPass123!')
        UserProfile.objects.create(user=self.user, target_role='Software Engineer')
        self.resume = ResumeAnalysis.objects.create(user=self.user, file='resumes/test.pdf', skills=['Python', 'Django'])
        self.client.force_login(self.user)

    def test_job_match_persists_grounded_score(self):
        response = self.client.post(reverse('job-matcher'), {'title': 'Backend Engineer', 'company': 'Acme', 'job_description': 'Python Django SQL Docker developer'})
        self.assertEqual(response.status_code, 200)
        match = JobMatch.objects.get(user=self.user)
        self.assertIn('Python', match.matched_skills)
        self.assertGreaterEqual(match.score, 0)

    def test_application_belongs_to_authenticated_user(self):
        response = self.client.post(reverse('applications'), {'company': 'Acme', 'job_title': 'Engineer', 'status': 'Applied'})
        self.assertRedirects(response, reverse('applications'))
        self.assertTrue(JobApplication.objects.filter(user=self.user, company='Acme').exists())
