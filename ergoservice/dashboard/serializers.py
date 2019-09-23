

from rest_framework import serializers
from dashboard.models import Case


class CaseSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Case
		fields = '__all__'



