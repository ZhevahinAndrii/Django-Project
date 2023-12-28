from django.contrib import admin
from django.urls import path, include


from .handlers import page_not_found


urlpatterns = [
    path('admin/', admin.site.urls),
    path('women/', include('women_app.urls', namespace='women'))
]

handler404 = page_not_found
