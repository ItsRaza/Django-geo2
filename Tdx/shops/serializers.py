from rest_framework import serializers
from shops.models import Shop, Company
from rest_framework import viewsets


class ShopSerializer(serializers.ModelSerializer):

    distance = serializers.DecimalField(
        source='distance.km', max_digits=10, decimal_places=2, required=False, read_only=True)

    class Meta:
        model = Shop
        fields = ['id', 'name', 'address', 'location', 'distance']
        # read_only_fields = ['distance']


class CompanySerializer(serializers.ModelSerializer):
    shop = serializers.RelatedField(many=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'shop_id']
