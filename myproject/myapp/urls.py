# myapp/urls.py
from django.urls import path
from . import views  # Ensure you're importing from the same app (dot notation for the current directory)

urlpatterns = [
    path('questions/', views.question_view, name='question_view'),
    path('results/', views.results_view, name='results'),
]
