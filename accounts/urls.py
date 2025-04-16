from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.loging_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]
