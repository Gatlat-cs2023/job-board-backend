from django.shortcuts import render

from rest_framework import viewsets, filters
from .models import Job
from .serializers import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-posted_at')
    serializer_class = JobSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['location', 'category', 'job_type']

    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAdmin()]
        return [IsAuthenticated()]