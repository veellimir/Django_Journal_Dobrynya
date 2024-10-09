from rest_framework import serializers

from .models import UsersAttendance

class AttendanceSerializer(serializers.ModelSerializer):
    training_direction_name = serializers.SerializerMethodField()
    profile_surname = serializers.SerializerMethodField()

    class Meta:
        model = UsersAttendance
        fields = [
            "profile_surname",
            "training_direction_name",
            "date",
            "is_present",
        ]


    def get_training_direction_name(self, obj: UsersAttendance) -> str:
        return obj.direction.name if obj.direction else None


    def get_profile_surname(self, obj: UsersAttendance):
        user = obj.profile.user if obj.profile else None
        if user:
            return f"{user.first_name} {user.last_name}"
        return None

