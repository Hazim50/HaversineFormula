import numpy as np


R = 6371
def pol2cart(lat, long):
    lat, long = np.radians(lat), np.radians(long)
    return R*np.cos(lat) *np.cos(long),\
           R*np.cos(lat) *np.sin(long),\
           R*np.sin(lat)


def haversine_dist(point1, point2):
  point1_cart = np.array(pol2cart(*point1))
  point2_cart = np.array(pol2cart(*point2))
  euc_dist = np.linalg.norm(point1_cart-point2_cart)
  sin_theta_2 = euc_dist / (R * 2)
  theta_2 = np.arcsin(sin_theta_2)
  theta = 2*theta_2
  dist = R*theta
  return dist

gps1 = (38.0344047,32.4971160)
gps2 = (38.0354568,32.4970490)
print(haversine_dist(gps1,gps2))

