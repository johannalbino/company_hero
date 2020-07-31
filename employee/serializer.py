from rest_framework import serializers
from employee.models import Employee
from company.serializer import CompanySerializer
from common.serializer import AddressSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=True)
    company = CompanySerializer(many=True)

    class Meta:
        model = Employee
        fields = ['username', 'name', 'phone', 'email', 'address', 'company']
