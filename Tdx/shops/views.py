from .models import Shop
from rest_framework import viewsets
from .serializers import ShopSerializer
from rest_framework import generics
import geocoder
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.db.models.functions import Distance
# from django.contrib.gis.db.models.functions import Distance
from rest_framework.views import APIView


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    # def perform_create(self, serializer):
    #     address = serializer.initial_data['location']
    #     g = geocoder.google(address)
    #     latitude = g.latlng[0]
    #     longitude = g.latlng[1]
    #     pnt = 'POINT(' + str(longitude)+' '+str(latitude)+')'
    #     print(pnt)
    #     serializer.save(location=pnt)

    def get_queryset(self):
        qs = super().get_queryset()
        latitude = self.request.query_params.get('lat', None)
        longitude = self.request.query_params.get('lng', None)

        if latitude and longitude:
            pnt = GEOSGeometry(
                'POINT(' + str(longitude) + ' ' + str(latitude)+')', srid=4326)
            qs = Shop.objects.filter(location__dwithin=(pnt, 50000)).annotate(
                distance=Distance('location', pnt)).order_by('distance')
        return qs

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     latitude = self.request.query_params.get('lat', None)
    #     longitude = self.request.query_params.get('lng', None)
    #     # distance_q = self.request.query_params.get('dist', None)
    #     shop_list = list()
    #     if latitude and longitude:
    #         pnt = GEOSGeometry(
    #             'POINT(' + str(longitude) + ' ' + str(latitude)+')', srid=4326)
    #         # distance =
    #         qs = qs.annotate(distance=Distance(
    #             'location', pnt)).order_by('distance')
    #         # qs = Shop.objects.filter(
    #         #     distance__lt=(pnt, Distance(km=5)))

    #     return qs


# def findDist(self):
#     point = Shop.objects.get(id=1).location
#     for shop in Shop.objects.all().exclude(id=1).annotate(distance=Distance('location', point)):
#         print('{0} - {1}'.format(event.id, event.distance.m))


# class MyView(APIView):
#     def post(self, request, *args, **kwargs):
#         findDist()
#         return Response(data={"my_return_data": my_result})
