from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Organization, Event
from .serializers import OrganizationSerializer, EventSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class EventViewSetPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 10


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = EventViewSetPagination
    filter_backends = [OrderingFilter, DjangoFilterBackend, SearchFilter]
    ordering_fields = ['date']
    filterset_fields = ['date']
    search_fields = ['title']
    permission_classes = [IsAuthenticated]
