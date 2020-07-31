from django.db import models


class Address(models.Model):
    """
    Endereço fisico baseado no CEP
    """

    zip_code = models.CharField(
        'CEP',
        max_length=9
    )

    address = models.CharField(
        'Logradouro',
        max_length=255,
        blank=True,
    )

    neighborhood = models.CharField(
        'Bairro',
        max_length=255,
        blank=True
    )

    state = models.CharField(
        'Estado',
        max_length=2,
        blank=True
    )

    number = models.CharField(
        'Número',
        max_length=20,
        blank=True
    )

    complement = models.CharField(
        'Complemento',
        max_length=255,
        blank=True
    )

    def __str__(self):
        """
        Retorna  o objeto no formato de string
        """

        return self.zip_code

    class Meta:
        """
        Informações a mais sobre a classe
        """

        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"
        db_table = "company_hero_address"
