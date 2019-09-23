

from dashboard.models import Case
from rest_framework import viewsets, permissions
from .serializers import CaseSerializer
  

class CaseViewSet(viewsets.ModelViewSet):
	queryset = Case.objects.all()
	permission_classes = [
		permissions.AllowAny
	]
	serializer_class = CaseSerializer