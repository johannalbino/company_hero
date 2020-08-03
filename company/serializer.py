from rest_framework import serializers
from company.models import Company
from employee.models import Employee
from common.models import Address
from common.serializer import AddressSerializer


class CompanySerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False)
    employees = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ['name', 'fantasy_name', 'cnpj', 'address', 'employees']

    def create(self, validated_data):
        """
        Função para criar empresas na API
        """
        address = Address.objects.create(**validated_data['address'])
        del validated_data['address']

        company = Company.objects.create(address=address, **validated_data)
        return company

    def get_employees(self, obj):
        """
        Pega todos os usuários relacionado a empresa pelo ID
        """
        list_employee = list()
        for emp in Employee.objects.filter(company=obj.id):
            list_employee.append(dict(
                username=emp.username,
                name=emp.name,
                phone=emp.phone,
                email=emp.email
            ))
        return list_employee
