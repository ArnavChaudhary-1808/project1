# crud_app/urls.py
from django.urls import path
from .views import person_create_view, person_success_view

urlpatterns = [
    path('add-person/', person_create_view, name='person_create'),
    path('success/', person_success_view, name='person_success'),
]
