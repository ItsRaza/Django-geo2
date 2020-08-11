from .models import Shop
from rest_framework import viewsets
from .serializers import ShopSerializer
from rest_framework import permissions
import geocoder
from rest_framework.views import APIView


class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()

    def perform_create(self, serializer):
        address = serializer.initial_data['address']
        g = geocoder.google(address)
        latitude = g.latlng[0]
        longitude = g.latlng[1]
        pnt = 'POINT(' + str(longitude)+' '+str(latitude)+')'
        serializer.save(location=pnt)


def findDist(self):
    point = Shop.objects.get(id=1).location
    for shop in Shop.objects.all().exclude(id=1).annotate(distance=Distance('location', point)):
        print('{0} - {1}'.format(event.id, event.distance.m))


def add(a, b):
    return a+b


class MyView(APIView):
    def post(self, request, *args, **kwargs):
        my_result = addTwoNumber(request.data.get(
            'firstnum'), request.data.get('secondnum'))
        return Response(data={"my_return_data": my_result})
