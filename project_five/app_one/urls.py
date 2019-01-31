from django.urls import path
from app_one import views

app_name = 'app_one'

urlpatterns = [
    path('',views.index, name='index'),
    path('other/',views.other, name='other'),
    path('relative/',views.relative, name='relative'),
]