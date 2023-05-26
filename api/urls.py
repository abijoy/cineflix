from django.urls import include, path
from rest_framework import routers
from .views import PostViewSet, ToyViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'toys', ToyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]