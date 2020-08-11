from rest_framework import serializers
from shops.models import Shop


class ShopSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Shop
        fields = ['id', 'name', 'address', 'location']
        read_only_fields = ['location', ]
