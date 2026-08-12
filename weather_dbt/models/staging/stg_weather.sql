select
  time as observed_at,
  temperature_2m as temperature_celsius,
  latitude,
  longitude,
  city
from {{source('raw_weather','weather')}}