from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Task
from django.contrib.auth.models import User
import logging


class UserSerializer(serializers.ModelSerializer):
    logging.debug("user serializer")

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")

    def create(self, validated_data):
        logging.debug("user serializer")
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)

        tasks = []
        for i in range(3):
            task = Task(
                user=user,
                title=f"task{i}",
                is_done=False,
            )
            tasks.append(task)

        Task.objects.bulk_create(tasks)

        return user


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
