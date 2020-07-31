from rest_framework import serializers
from company.models import Company
from common.serializer import AddressSerializer


class CompanySerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'fantasy_name', 'cnpj', 'address']
