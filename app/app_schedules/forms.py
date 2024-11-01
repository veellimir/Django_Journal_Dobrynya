from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    days_of_week = forms.MultipleChoiceField(
        choices=Event.DAYS_OF_WEEK_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Event
        fields = '__all__'

    def clean_days_of_week(self):
        days = self.cleaned_data.get('days_of_week')
        return ','.join(days)
