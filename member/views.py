from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
from member.models import Member
from member.serializers import memberSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse


class memberListView(APIView):
    def get(self, request, format=None):
        members = Member.objects.all()
        serializer = memberSerializer(members, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = memberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class memberDetails(APIView):
    def get(self, request, pk, format=None):
        member = Member.objects.filter(email=pk)
        serializer = memberSerializer(member, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            members = Member.objects.get(email=pk)
            serializer = memberSerializer(members, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Member.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def delet(self, request, pk, format=None):
        try:
            members = Member.objects.get(email=pk)
            members.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Member.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

class memberByAntenneDetails(APIView):
    def get(self, request, pk, format=None):
        member = Member.objects.filter(antenne=pk)
        serializer = memberSerializer(member, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            members = Member.objects.get(antenne=pk)
            serializer = memberSerializer(members, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Member.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def delet(self, request, pk, format=None):
        try:
            members = Member.objects.get(antenne=pk)
            members.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Member.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
