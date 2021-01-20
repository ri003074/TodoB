from django.urls import include
from django.urls import path
from todob.views import TaskViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register("tasks", TaskViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
