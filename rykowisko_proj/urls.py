from django.contrib import admin
from django.urls import path
from django.urls import include

from django.contrib.auth import views
from moj_blog import views as bv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('moj_blog.urls')),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/rejestracja/', bv.rejestracja_view, name='rejestracja'),
]
