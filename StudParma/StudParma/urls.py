from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    # При переходе на главную страницу вызывается urls.py(из main)
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('psumaps/', include('psumaps.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
