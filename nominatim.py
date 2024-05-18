# Muhammad Jaleed (12248353)
# Jeneesh Patel (1225422)

import requests

def gps_coordinate(city):
    """
    Fetch GPS coordinates for a given city using the Nominatim geocoding web service.
    
    Args:
    city (str): The city name to fetch coordinates for.

    Returns:
    dict: A dictionary with 'latitude' and 'longitude' as keys and the respective coordinates as float values.

    Example:
    >>> gps_coordinate("Cairns")
    {'latitude': -16.92, 'longitude': 145.777}
    """
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {'q': city, 'format': 'json'}
    response = requests.get(base_url, params=params)
    print(response)
    data = response.json()[0]
    return {'latitude': float(data['lat']), 'longitude': float(data['lon'])}

# Call the function and print the result
city = "Cairns"
coordinates = gps_coordinate(city)
print("GPS Coordinates for", city, ":", coordinates)
# Assert statements for testing
# assert gps_coordinate("Cairns") == {'latitude': -16.92, 'longitude': 145.777}, "Test failed for Cairns"
