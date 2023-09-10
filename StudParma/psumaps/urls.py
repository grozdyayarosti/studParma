from django.urls import path, include
from . import views
from .views import Register

# Массив с отслеживаемыми url-адресами
urlpatterns = [
    # path('', views.start_form, name='start_form'),                              # домашняя страница
    # path('auth/', views.test_login, name='auth_form'),
    # path('registration', views.RegisterView.as_view(), name='registration_form'),
    # path('registration/', views.test_reg, name='registration_form'),
    # path('registration', views.check, name='check'),


    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register')


]

