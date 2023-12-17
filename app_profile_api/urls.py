from django.urls import path
from app_profile_api import views

urlpatterns = [path("hello-view/", views.HelloAPIView.as_view())]
