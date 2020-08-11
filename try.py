import geocoder

g = geocoder.google('Bellagio Las Vegas, NV')
latitude = g.latlng[0]
longitude = g.latlng[1]
pnt = 'POINT(' + str(longitude)+' '+str(latitude)+')'
print(pnt)
