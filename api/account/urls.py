from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account import views

router = DefaultRouter()
router.register('profile', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls))
]
