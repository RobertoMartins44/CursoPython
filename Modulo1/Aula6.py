#Funções
import pandas as pd
from geopy import geocode
from math import pi, sqrt

def calc_area (point1,point2):
  x1,y1 = point1
  x2,y2 = point2
  return (x1*y2 - y1*x2) / 2


#lambda função anonima
x = 5
y = 8
soma = lambda x, y: x + y


