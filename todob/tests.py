from django.test import TestCase
from .models import Task


class TaskModelTest(TestCase):
    def setUp(self):
        Task.objects.create(title="abc")

    def test_task(self):
        task_title = Task.objects.get(title="abc")

        self.assertEqual(task_title.title, "abc")
