from rest_framework import serializers
from common.models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['zip_code', 'address', 'neighborhood', 'state', 'number',
                  'complement']
