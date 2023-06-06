from rest_framework import serializers
from users.serializers import CustomUserSerializer
from .models import Organization, Event


class OrganizationSerializer(serializers.ModelSerializer):
    users = CustomUserSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = ['title', 'description', 'address', 'postcode', 'users']


class EventSerializer(serializers.ModelSerializer):
    organizations = OrganizationSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['title', 'description', 'organizations', 'image', 'date']
