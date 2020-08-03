from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from common.models import Log, Address
from company.models import Company
from employee.models import Employee
from employee.tests.mocks import EMPLOYEE_CREATE_PAYLOAD, EMPLOYEE_GET


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

        self.employee = Employee.objects.create(
            username="teste",
            name="Johann Albino",
            phone="31995494755",
            email="johann@gmail.com",
            date_birth="1995-06-17",
            cpf="13345678917",
            address=address
        )
        self.employee.company.add(Company.objects.get(id=self.company.id))
        self.employee.save()

    def tearDown(self):
        Log.objects.all().delete()

    def test_create_employee(self):

        EMPLOYEE_CREATE_PAYLOAD['company'][0].update({'id': self.company.id})
        response = self.client.post(
            self.url,
            data=EMPLOYEE_CREATE_PAYLOAD,
            headers=self.headers,
            format='json'
        )

        self.assertEqual(
            Employee.objects.filter(cpf=EMPLOYEE_CREATE_PAYLOAD['cpf']).count(),
            1
        )
        self.assertEqual(
            Log.objects.all().count(),
            2
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_employee(self):
        response = self.client.get(
            self.url,
            headers=self.headers,
            format='json'
        )
        EMPLOYEE_GET['results'][0]['company'][0].update({'id': self.company.id})
        EMPLOYEE_GET['results'][0].update({'id': self.employee.id})
        self.assertEqual(
            response.json(),
            EMPLOYEE_GET
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_employee(self):
        url = reverse('funcionarios-detail', kwargs={'pk': str(self.employee.pk)})
        response = self.client.delete(
            url,
            headers=self.headers,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Employee.objects.filter(cpf='13345678917').count(),
            0
        )
