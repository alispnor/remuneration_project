from rest_framework import viewsets
from .models import UnitRemuneration, UnitRemunerationAggregated
from .serializers import UnitRemunerationSerializer, UnitRemunerationAggregatedSerializer

class UnitRemunerationViewSet(viewsets.ModelViewSet):
    queryset = UnitRemuneration.objects.all()
    serializer_class = UnitRemunerationSerializer

class UnitRemunerationAggregatedViewSet(viewsets.ModelViewSet):
    queryset = UnitRemunerationAggregated.objects.all()
    serializer_class = UnitRemunerationAggregatedSerializer
