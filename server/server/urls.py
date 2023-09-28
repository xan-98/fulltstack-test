from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/chat/', include('chat.urls')),
    path('api/v1/user/', include('user.urls')),
]
