from rest_framework import serializers
from employee.models import Employee
from company.models import Company
from common.models import Address
from common.serializer import AddressSerializer
from common.exceptions import (ParameterInvalid,
                               CompanyNonexistent)


class CompanySerializerEmployee(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=False)
    fantasy_name = serializers.CharField(required=False)
    cnpj = serializers.CharField(required=False)

    class Meta:
        model = Company
        fields = ['id', 'name', 'fantasy_name', 'cnpj']


class EmployeeSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False)
    company = CompanySerializerEmployee(many=True)

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        """
        Função para criar dados do usuário na API
        """
        list_company = list()
        try:
            address = Address.objects.create(**validated_data['address'])
            del validated_data['address']
        except KeyError:
            raise ParameterInvalid()

        try:
            for company in validated_data['company']:
                list_company.append(Company.objects.get(id=company['id']))
            del validated_data['company']
        except KeyError:
            raise ParameterInvalid()
        except Company.DoesNotExist:
            raise CompanyNonexistent()

        employee = Employee(**validated_data)
        employee.address = address
        employee.save()

        employee.company.set(list_company)
        return employee
