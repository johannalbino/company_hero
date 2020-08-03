from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from common.models import Log, Address
from company.models import Company
from employee.tests.mocks import EMPLOYEE_CREATE_PAYLOAD


class TestEmployee(APITestCase):

    def setUp(self):
        self.url = reverse('funcionarios-list')
        self.headers = {"Content-Type": "application/json"}

        address = Address.objects.create(
            zip_code="30140000",
            address="Avenida Brasil",
            neighborhood="Santa Efigênia",
            state="MG",
            number="255",
            complement="Predio"
        )

        self.company = Company.objects.create(
            name='Teste by Test',
            fantasy_name='Test',
            cnpj='01234567890123',
            address=address
        )
