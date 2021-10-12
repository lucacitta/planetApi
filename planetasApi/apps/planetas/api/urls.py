from django.urls import path
from apps.planetas.api.api import planetas_api_view, planetas_api_detail_view

urlpatterns = [
    path('', planetas_api_view, name='planetas api'),
    path('<int:pk>/', planetas_api_detail_view, name='planetas detail api')
]