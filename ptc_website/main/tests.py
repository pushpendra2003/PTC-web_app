from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task, UserProfile

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.task = Task.objects.create(task_type='shortlink', description='Test task', reward=10.00)

    def test_task_creation(self):
        self.assertEqual(self.task.task_type, 'shortlink')
        self.assertEqual(self.task.description, 'Test task')

class UserProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user_profile = UserProfile.objects.create(user=self.user, ip_address='127.0.0.1')

    def test_ip_address(self):
        self.assertEqual(self.user_profile.ip_address, '127.0.0.1')
