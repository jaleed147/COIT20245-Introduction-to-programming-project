def display_menu():
    """
    Display the menu options to the user.
    """
    print("Help\n====")
    print("The following commands are recognised.")
    print("Display help wildlife> help")
    print("Display animal species in a city wildlife> species <CityName>")
    print("Display animal sightings in a city wildlife> sightings <CityName> <TaxonID>")
    print("Display venomous species wildlife> species <CityName> venomous")
    print("Exit the application wildlife> exit")

def search_species(city):
    """
    Return a list of species dictionaries for the specified city.
    Now uses GPS coordinates from the gps(city) function.
    """
    coordinates = gps(city)
    # Use coordinates in future development
    return [
        {"Species": {"AcceptedCommonName": "dolphin", "PestStatus": "Nil"}},
        {"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}}
    ]

def display_species(species_list):
    """
    Print a list of species to the screen.
    """
    for species in species_list:
        print(f"{species['Species']['AcceptedCommonName']} - {species['Species']['PestStatus']}")

def search_sightings(taxonid, city):
    """
    Return a list of animal sightings dictionaries for the specified city and species TaxonID.
    Currently returns a stubbed response.
    """
    return [{"properties": {"StartDate": "1999-11-15", "LocalityDetails": "Tinaroo"}}]

def display_sightings(sightings):
    """
    Print a list of animal sightings to the screen.
    """
    for sighting in sightings:
        print(f"Date: {sighting['properties']['StartDate']}, Location: {sighting['properties']['LocalityDetails']}")

def filter_venomous(species_list):
    """
    Filter and return only venomous species from the list.
    """
    return [species for species in species_list if species['Species']['PestStatus'] == 'Venomous']

def gps(city):
    """
    Return GPS coordinates for the specified city.
    Currently returns a stubbed response for Brisbane.
    """
    return {"latitude": -27.4689682, "longitude": 153.0234991}

def main():
    while True:
        command = input("wildlife> ").strip().lower()
        parts = command.split()
        if parts[0] == 'species' and 'venomous' in parts:
            city = ' '.join(parts[1:-1])
            species_list = search_species(city)
            venomous_species = filter_venomous(species_list)
            display_species(venomous_species)
        elif parts[0] == 'species':
            city = ' '.join(parts[1:])
            species_list = search_species(city)
            display_species(species_list)
        elif parts[0] == 'sightings':
            city = ' '.join(parts[1:-1])
            taxonid = parts[-1]
            sightings = search_sightings(taxonid, city)
            display_sightings(sightings)
        elif command == 'help':
            display_menu()
        elif command == 'exit':
            print("Exiting the application.")
            break
        else:
            print("Invalid command. Type 'help' for a list of commands.")

main()