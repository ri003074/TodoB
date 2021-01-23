from django.contrib.auth.models import User
from django.test import TestCase
from .models import Task


class TaskModelTest(TestCase):
    def setUp(self):
        user = User()
        user.save()
        Task.objects.create(title="abc", user=user)

    def test_task(self):
        task_title = Task.objects.get(title="abc")

        self.assertEqual(task_title.title, "abc")
