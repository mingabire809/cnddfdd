from django.shortcuts import render

# Create your views here.
from antenne.models import Antenne
from antenne.serializers import antenneSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from rest_framework.views import APIView


class antenneListView(APIView):
    def get(self, request, format=None):
        antenne = Antenne.objects.all()
        serializer = antenneSerializer(antenne, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = antenneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class antenneDetails(APIView):
    def get(self, request, pk, format=None):
        antenne = Antenne.objects.filter(name=pk)
        serializer = antenneSerializer(antenne, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            antenne = Antenne.objects.get(name=pk)
            serializer = antenneSerializer(antenne, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Antenne.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def delet(self, request, pk, format=None):
        try:
            antenne = Antenne.objects.get(name=pk)
            antenne.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Antenne.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)