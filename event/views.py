from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
from event.models import Event
from event.serializers import eventSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse


class eventListView(APIView):
    def get(self, request, format=None):
        events = Event.objects.all()
        serializer = eventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = eventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class eventDetails(APIView):
    def get(self, request, pk, format=None):
        event = Event.objects.filter(eventName=pk)
        serializer = eventSerializer(event, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            events = Event.objects.get(eventName=pk)
            serializer = eventSerializer(events, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Event.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def delet(self, request, pk, format=None):
        try:
            event = Event.objects.get(eventName=pk)
            event.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Event.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)