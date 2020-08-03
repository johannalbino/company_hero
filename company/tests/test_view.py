from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from company.models import Company
from common.models import Log, Address
from company.tests.mocks import COMPANY_CREATE_PAYLOAD, COMPANY_GET


class TestCompany(APITestCase):

    def setUp(self):
        self.url = reverse('empresas-list')
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

    def tearDown(self):
        Log.objects.all().delete()
        Company.objects.all().delete()

    def test_create(self):
        response = self.client.post(
            self.url,
            data=COMPANY_CREATE_PAYLOAD,
            headers=self.headers,
            format='json'
        )
        self.assertEqual(
            Company.objects.filter(cnpj=COMPANY_CREATE_PAYLOAD['cnpj']).count(),
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

    def test_list(self):
        response = self.client.get(
            self.url,
            headers=self.headers,
            format='json'
        )

        self.assertEqual(
            response.json(),
            COMPANY_GET
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete(self):
        url = reverse('empresas-detail', kwargs={'pk': str(self.company.pk)})
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
            Company.objects.filter(cnpj='01234567890123').count(),
            0
        )
