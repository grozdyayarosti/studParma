from django.urls import path
from . import views

# Массив с отслеживаемыми url-адресами
urlpatterns = [
    path('', views.news_home, name='news_home'),                                # домашняя страница
    path('create', views.create, name='create'),                                # создание новости
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),       # страница с динамическим параметром
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),# обновление новости
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete') # удаление новости
]

