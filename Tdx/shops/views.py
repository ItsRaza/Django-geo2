from .models import Shop
from rest_framework import viewsets
from .serializers import ShopSerializer
from rest_framework import permissions
from rest_framework.views import APIView


class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    permission_classes = [permissions.IsAuthenticated]


def findDist(self):
    point = Shop.objects.get(id=1).location
    for shop in Shop.objects.all().exclude(id=1).annotate(distance=Distance('location', point)):
        print('{0} - {1}'.format(event.id, event.distance.m))


class MyView(APIView):
    def post(self, request, *args, **kwargs):
        my_result = findDist()
        return Response(data={"my_return_data": my_result})
