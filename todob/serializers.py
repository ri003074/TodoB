from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    # use "user_id" then error. why??
    user_uid = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True
    )

    def create(self, validated_date):
        validated_date["user"] = validated_date.get("user_uid", None)

        if validated_date["user"] is None:
            raise serializers.ValidationError("user not found.")

        del validated_date["user_uid"]

        return Task.objects.create(**validated_date)

    class Meta:
        model = Task
        fields = ("id", "title", "user", "user_uid", "is_done")
