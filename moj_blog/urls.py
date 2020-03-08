from django.urls import path
from . import views

app_name='moj_blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('moj_blog/nowy', views.nowy, name='nowy'),
    path('moj_blog/<int:pk>', views.wpis, name='wpis'),
    path('moj_blog/<int:pk>/edit/', views.edycja, name='edycja'),
]



#localhost:8000/5/