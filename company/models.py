from django.db import models
from common.models import Address


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    fantasy_name = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14)
    address = models.OneToOneField(Address, on_delete=models.PROTECT)

    class Meta:
        db_table = 'company_hero_company'

    def __str__(self):
        return self.name
