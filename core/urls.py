from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('auth/redirect/', views.auth_redirect),
    path('auth/callback/', views.auth_callback),
    path('', views.home),
    path('area/<str:area>/', views.area),
]
