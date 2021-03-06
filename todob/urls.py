from django.urls import include
from django.urls import path
from todob.views import TaskViewSet, UserViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register("tasks", TaskViewSet)
router.register("users", UserViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
