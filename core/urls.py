from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('edit/<str:pk>', views.edit, name='edit'),
    path('active_completed/<str:pk>', views.active_completed, name='active_completed')
]