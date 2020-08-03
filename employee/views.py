from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters import rest_framework as filters
from employee.models import Employee
from employee.filter import EmployeeFilter
from employee.serializer import EmployeeSerializer


class EmployeeView(viewsets.ModelViewSet):
    """
    View para retornar informações do funcionário.
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EmployeeFilter

    def get_queryset(self):
        return Employee.objects.all()

    def list(self, request, *args, **kwargs):
        """
        Função que retornar a lista de funcionários.
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
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
