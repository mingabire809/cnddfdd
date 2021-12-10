from event.models import Event
from rest_framework import serializers


class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['eventName', 'location', 'date', 'program', 'participant']
