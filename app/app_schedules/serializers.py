from typing import Dict

from rest_framework import serializers

from app.app_schedules.models import Event, CancelEvents
from app.users.serializers import ProfileAdminSerializer


class EventSerializer(serializers.ModelSerializer):
    training_direction_name = serializers.SerializerMethodField()
    teacher = ProfileAdminSerializer(many=True, source="coaches")

    class Meta:
        model = Event
        fields = [
            "training_direction_name",
            "competition_name",
            "title",
            "teacher",
            "start_time",
            "end_time",
            "days_of_week",
            "elem_color",
            "category",
            "event_date"
        ]

    def get_training_direction_name(self, obj: Event) -> str:
        # Если training_direction_name пустое, используем competition_name
        if obj.name:
            return obj.name.name
        elif obj.competition_name:
            return obj.competition_name
        return None

    def to_representation(self, instance: Event) -> Dict[str, any]:
        representation = super().to_representation(instance)
        representation["start_time"] = instance.start_time.strftime("%H:%M")
        representation["end_time"] = instance.end_time.strftime("%H:%M")
        representation["days_of_week"] = instance.days_of_week.split(",") if instance.days_of_week else []

        if instance.event_date:
            representation["event_date"] = instance.event_date.strftime("%Y-%m-%d")
        return representation



class CancelEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CancelEvents
        fields = [
            "cancelled_title",
            "cancelled_date",
            "cancelled_red_color",
            "description"
        ]