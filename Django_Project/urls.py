from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy

from .handlers import page_not_found


urlpatterns = [
    path('admin/', admin.site.urls),
    path('women/', include('women_app.urls', namespace='women')),
    path('__debug__/',include('debug_toolbar.urls'))
]

handler404 = page_not_found
admin.site.site_header = gettext_lazy('Панель адміністрування')
admin.site.index_title = 'Відомі жінки світу'

