from django.urls import path

from . import views


app_name = "women"
urlpatterns = [
    path('', views.index, name='index'),
    path('archive1/<int:year1>/<int:year2>', views.archive, name='archive')
]