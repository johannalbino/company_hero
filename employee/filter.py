from django_filters import rest_framework as filters
from employee.models import Employee


class EmployeeFilter(filters.FilterSet):
    """
    Metodo para aplicar filtros na pesquisa de dados
    """

    username = filters.CharFilter(
        lookup_expr='icontains'
    )

    name = filters.CharFilter(
        lookup_expr='icontains'
    )

    phone = filters.CharFilter(
        lookup_expr='icontains'
    )

    email = filters.CharFilter(
        lookup_expr='icontains'
    )

    cpf = filters.CharFilter(
        lookup_expr='icontains'
    )

    class Meta:
        model = Employee
        fields = ['username', 'name', 'phone', 'email', 'cpf']
