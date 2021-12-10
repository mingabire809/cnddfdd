from rest_framework import serializers
from member.models import Member


class memberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['firstName', 'lastName', 'phoneNumber', 'email', 'antenne']
