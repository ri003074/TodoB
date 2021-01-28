from django.contrib.auth.models import User
from django.test import RequestFactory
from django.test import TestCase
from rest_framework.test import force_authenticate
from .models import Task
from .views import TaskViewSet


class TaskModelTest(TestCase):
    def setUp(self):
        user = User()
        user.save()
        Task.objects.create(title="abc", user=user)

    def test_task(self):
        task_title = Task.objects.get(title="abc")

        self.assertEqual(task_title.title, "abc")


class TestTaskViewSet(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="kenta", password="kawamoto", email="kenta@gmail.com"
        )
        Task.objects.create(title="task1-kenta", user=self.user)
        Task.objects.create(title="task2-kenta", user=self.user, is_done=True)
        Task.objects.create(title="task3-kenta", user=self.user)

    def test_task_viewset(self):
        request = self.factory.get("/api/tasks/")
        force_authenticate(request, user=self.user)
        response = TaskViewSet.as_view({"get": "list"})(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["id"], 1)
        self.assertEqual(response.data[0]["title"], "task1-kenta")
        self.assertEqual(response.data[0]["user"]["id"], 1)
        self.assertEqual(response.data[0]["user"]["username"], "kenta")
        self.assertEqual(response.data[0]["is_done"], False)

        self.assertEqual(response.data[1]["id"], 2)
        self.assertEqual(response.data[1]["title"], "task2-kenta")
        self.assertEqual(response.data[1]["user"]["id"], 1)
        self.assertEqual(response.data[1]["user"]["username"], "kenta")
        self.assertEqual(response.data[1]["is_done"], True)