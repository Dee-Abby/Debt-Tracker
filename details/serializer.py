from rest_framework import serializers
from .models import *

class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ['id', 'description', 'amount', 'owner', 'entity', 'date_borrowed']