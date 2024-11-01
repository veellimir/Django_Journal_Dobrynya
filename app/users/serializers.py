from rest_framework import serializers

from app.users.models import ProfileAdmin


class ProfileAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileAdmin
        fields = ["id", 'name', "surname", "patronymic"]