from django.db import models
from common.models import Address
from company.models import Company


class Employee(models.Model):

    username = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    company = models.ManyToManyField(Company)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        db_table = 'company_employes'
