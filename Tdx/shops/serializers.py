from rest_framework import serializers
from shops.models import Shop, Company
from rest_framework import viewsets
from django.core.serializers import serialize
import json


class ShopSerializer(serializers.ModelSerializer):

    distance = serializers.DecimalField(
        source='distance.km', max_digits=10, decimal_places=2, required=False, read_only=True)

    # serialize('geojson', Shop.objects.all(),
    #           geometry_field='location', fields=('name', 'address'))

    class Meta:
        model = Shop
        fields = ['id', 'name', 'address',
                  'distance', 'coordinates']

        # read_only_fields = ['distance']


class CompanySerializer(serializers.ModelSerializer):
    shop_set = ShopSerializer(many=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'shop_set']

    def create(self, validated_data):
        shop_validated_data = validated_data.pop('shop_set')
        company = Company.objects.create(**validated_data)
        shop_set_serializer = self.fields['shop_set']
        for each in shop_validated_data:
            each['company'] = company
        shops = shop_set_serializer.create(shop_validated_data)
        return company

    # def to_representation(self, obj):
    #     data = super().to_representation(obj)

    #     strr = json.dumps(
    #         {'lat': data['location']['coordinates'][0], 'long': data['location']['coordinates'][1]})
    #     st = strr.replace("'", "\\")
    #     retData = json.loads(st)
    #     data['location'] = retData
    #     return data
