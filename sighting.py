from nominatim import gps_coordinate
from wildlife import get_species_list 
from wildlife import get_surveys_by_species
from wildlife import sort_by_date

def gps(city):
    """
    Fetch GPS coordinates for a given city.
    
    Args:
    city (str): The city name to fetch coordinates for.

    Returns:
    dict: A dictionary with 'latitude' and 'longitude'.
    """
    return gps_coordinate(city)

# Test the function by printing the GPS coordinates of a city
print(gps("Cairns"))
print(gps("Cairns Regional"))

RADIUS = 100000 
def search_species(city):
    """
    Search for species in a 100 km radius around the given city.
    
    Args:
    city (str): The city name to search around.

    Returns:
    list: A list of species found.
    """
    coordinates = gps(city)
    species_list = get_species_list((coordinates['latitude'], coordinates['longitude']), RADIUS)
    return species_list

def search_sightings(taxonid, city):
    coordinates = gps(city)
    surveys = get_surveys_by_species((coordinates['latitude'], coordinates['longitude']), RADIUS, taxonid)
    incidental_surveys = [survey for survey in surveys if survey.get('SiteCode') == 'INCIDENTAL']
    return incidental_surveys


def display_sightings(sightings):
    sorted_sightings = sort_by_date(sightings)
    for sighting in sorted_sightings:
        print(sighting)
