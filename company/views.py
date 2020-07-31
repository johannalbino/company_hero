from rest_framework.viewsets import ModelViewSet
from company.models import Company
from rest_framework.response import Response
from django_filters import rest_framework as filters
from company.filter import CompanyFilter
from company.serializer import CompanySerializer


class CompanyView(ModelViewSet):
    """
    View para retornar informações da empresa e seus funcionários
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CompanyFilter

    def get_queryset(self):
        return Company.objects.all()

    def list(self, request, *args, **kwargs):
        """
        Função para retornar a listagem de empresas
        """
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Função para criar novos funcionários
        """

        pass

    def perform_create(self, serializer):
        serializer.save()

