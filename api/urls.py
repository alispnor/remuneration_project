from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UnitRemunerationViewSet, UnitRemunerationAggregatedViewSet

router = DefaultRouter()
router.register(r'remunerations', UnitRemunerationViewSet)
router.register(r'remunerations-aggregated', UnitRemunerationAggregatedViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
