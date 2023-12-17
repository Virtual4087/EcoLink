from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_view, name="default_view"),
    path('logout', views.logout_view, name="logout"),
]
