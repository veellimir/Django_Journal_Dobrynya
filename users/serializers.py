from rest_framework import serializers

from users.models import ProfileAdmin


class ProfileAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileAdmin
        fields = ["id", 'name', "surname", "patronymic"]