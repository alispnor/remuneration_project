from rest_framework import serializers
from .models import UnitRemuneration, UnitRemunerationAggregated

class UnitRemunerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitRemuneration
        fields = '__all__'

class UnitRemunerationAggregatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitRemunerationAggregated
        fields = '__all__'
