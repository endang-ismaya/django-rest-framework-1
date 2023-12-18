from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app_profile_api import views

router = DefaultRouter()
router.register(
    prefix="hello-viewset",
    viewset=views.HelloViewSet,
    basename="hello-viewset",
)
router.register(
    prefix="profiles",
    viewset=views.UserProfileViewSet,
    basename="app_profile_api__profiles",
)
router.register(
    prefix="feeds",
    viewset=views.UserProfileFeedViewSet,
    basename="app_profile_api__feeds",
)

urlpatterns = [
    path("hello-view/", views.HelloAPIView.as_view()),
    path("login/", views.UserLoginApiView.as_view()),
    path("", include(router.urls)),
]
