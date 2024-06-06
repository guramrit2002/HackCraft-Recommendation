from rest_framework.serializers import ModelSerializer
from .models import HackathonRecord


class HackathonRecordSerializer(ModelSerializer):
    
    class Meta:
        model = HackathonRecord
        fields = '__all__'