from math import radians, cos, sin, asin, sqrt

#haversine. It’s going to take 4 arguments, which will be the longitude and latitude of the two points whose distance we need to find.

def haversine(lon1, lat1, lon2, lat2):

#convert degrees to radians
      lon1 = radians(lon1)
      lat1 = radians(lat1)
      lon2 = radians(lon2)
      lat2 = radians(lat2
)
#find the difference between the two longitudes and latitudes
      dlon = lon2 - lon1
      dlat = lat2 - lat1

      a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
      distance = 2 * asin(sqrt(a)) * 6371 #6371 is the radius of the Earth
      print(distance)
      return distance


haversine(74.0059, 40.7128, 0.1278, 51.5074)
