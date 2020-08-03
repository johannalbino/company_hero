from django.db import models
from common.models import Address
from company.models import Company


class Employee(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    username = models.CharField(
        'Username',
        max_length=20,
        unique=True
    )
    name = models.CharField(
        'Nome completo',
        max_length=200
    )
    phone = models.CharField(
        'Telefone',
        max_length=11
    )
    email = models.CharField(
        'Email',
        max_length=255
    )
    date_birth = models.DateField(
        'Data de Nascimento'
    )
    cpf = models.CharField(
        'CPF',
        max_length=11,
        unique=True
    )
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE
    )
    company = models.ManyToManyField(
        Company
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        db_table = 'company_hero_employees'
