import requests

def get_species_list(coordinate, radius):
    """
    Retrieve a list of species in an area defined by a circle with given coordinates and radius.
    
    Args:
    coordinate (tuple): The latitude and longitude of the center of the circle.
    radius (int): The radius of the circle in meters.

    Returns:
    list: A list of dictionaries, each containing species information.
    """
    base_url = "https://apps.des.qld.gov.au/species/"
    params = {
        'op': 'getspecieslist',
        'kingdom': 'animals',
        'circle': f"{coordinate[0]},{coordinate[1]},{radius}"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    species_list = [species['Species'] for species in data['SpeciesSightingSummariesContainer']['SpeciesSightingSummary']]
    return species_list

def get_surveys_by_species(coordinate, radius, taxonid):
    base_url = "https://apps.des.qld.gov.au/species/"
    params = {
        'op': 'getsurveysbyspecies',
        'taxonid': taxonid,
        'circle': f"{coordinate[0]},{coordinate[1]},{radius}"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    surveys = [survey['properties'] for survey in data['features']]
    return surveys

def earliest(sightings):
    return min(sightings, key=lambda x: x['StartDate'])

def sort_by_date(sightings):
    return sorted(sightings, key=lambda x: x['StartDate'])

# Test the function by printing the species list for a specific coordinate and radius
print(get_species_list((-16.92, 145.777), 100000))
