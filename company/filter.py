from django_filters import rest_framework as filters
from company.models import Company


class CompanyFilter(filters.FilterSet):
    """
    Classe para aplicar filtro em empresas quando solicitado
    """

    name = filters.CharFilter(lookup_expr='icontains')
    fantasy_name = filters.CharFilter(lookup_expr='icontains')
    cnpj = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Company
        fields = ['name', 'fantasy_name', 'cnpj']
