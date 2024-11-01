from django import forms

from .models import TaskUser


class TaskUserForm(forms.ModelForm):
    class Meta:
        model = TaskUser
        fields = [
            "user",
            "title",
            "description"
        ]
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),

            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название задачи'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Введите описание задачи'
            }),
        }

