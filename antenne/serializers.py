from antenne.models import Antenne
from rest_framework import serializers


class antenneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Antenne
        fields = ['name', 'county']
