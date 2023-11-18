from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CustomerViewSet, ProjectViewSet

router = DefaultRouter()
router.register('user', UserViewSet)
router.register('customer', CustomerViewSet)
router.register('project', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
