from django.contrib.gis.geos import Point
from django.db.models.manager import Manager
from django.contrib.gis.measure import Distance
from django.contrib.gis.db import models
import json


class Company(models.Model):
    name = models.CharField(max_length=200, default='Company', null=True)

    def __unicode__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=200, default="bla")
    address = models.CharField(max_length=300, default='blabla')
    location = models.PointField(null=True, blank=True, geography=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True)
    test = models.IntegerField(null=True, default=14)
    # objects = models.GeoManager(null=True)

    @property
    def coordinates(self):
        loc = self.location
        res = json.dumps({'Lat': loc[1], 'long': loc[0]})
        retData = json.loads(res)
        return retData

    # @property
    # def latitude(self):
    #     return self.location.y

    # class Meta:
    #     unique_together = ('company', 'name')

    # def __str__(self):
    #     return self.location

    # def insertTwoPoints(self):
    #     # point = Point(x=12.734534, y=77.2342)
    #     # shop1 = Shop()
    #     # shop1.location = point
    #     # shop1.save()
    #     point1 = Point(x=15.734534, y=79.2342)
    #     shop2 = Shop()
    #     shop2.location = point
    #     shop2.save()

    # shop = models.ForeignKey(
    # Shop, on_delete=models.CASCADE, null=True, related_name='company')

    # order_by = 'name'

    # def __unicode__(self):
    #     return '%s' % (self.name)

    # def __str__(self):
    #     return self.shop.name or ''
