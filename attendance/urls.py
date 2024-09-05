from django.urls import path
from .views import TrainingDirectionsListView

urlpatterns = [
    path('training-directions/', TrainingDirectionsListView.as_view(), name='training_directions_list'),
]
