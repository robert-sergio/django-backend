from rest_framework import serializers
from core.models import Test

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = [*(f.name for f in Test._meta.get_fields()), 'pk']