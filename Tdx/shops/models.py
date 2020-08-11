from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.contrib.gis.db import models


class Shop(models.Model):
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=300, null=True)
    location = models.PointField(null=True, blank=True)

    def __str__(self):
        return self.location

    # def insertTwoPoints(self):
    #     # point = Point(x=12.734534, y=77.2342)
    #     # shop1 = Shop()
    #     # shop1.location = point
    #     # shop1.save()
    #     point1 = Point(x=15.734534, y=79.2342)
    #     shop2 = Shop()
    #     shop2.location = point
    #     shop2.save()
