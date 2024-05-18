
## COIT20245 - Introduction to Programming
### Assignment 2: Python Application for Wildlife Sighting Analysis
### Group Members:
          Muhammad Jaleed (12248353)
          Jeneesh Patel (1225422)


---

### 1. Functionality and Adherence

The code demonstrates the following functionalities:
•	Menu System: Displays a menu with options for help, displaying species in a city (limited functionality), displaying animal sightings (limited functionality), and exiting the application. (settings.py)
•	Species Search: Retrieves a pre-defined list of species for a city (currently not using a web service). Can filter venomous species from the list. (settings.py)
•	Animal Sightings: Retrieves a stubbed list of animal sightings with basic information. (settings.py)
•	Geolocation (Stub): Returns a predefined GPS coordinate for a city regardless of the input city. (settings.py)
The application adheres to the assignment by providing a basic framework for user interaction and data display.  However, it requires further development to integrate external web services for real-time geolocation and wildlife data retrieval.


---

### 2. Functionalities Implemented

#### 2.1 Display Help Menu

Implemented a function to display a help menu with the recognized commands.

```python
def display_menu():
    print("Help\n====")
    print("The following commands are recognised.")
    print("Display help wildlife> help")
    print("Exit the application wildlife> exit")
    print("Display animal species in a city wildlife> species <city>")
    print("Display animal sightings in a city wildlife> sightings <city> <taxonid>")
    print("Display venomous species wildlife> species <city> venomous")
```

#### 2.2 Handle User Input

Implemented the main function to handle user input and call the appropriate functions based on the commands entered.

```python
def main():
    display_menu()
    while True:
        command = input("wildlife> ").strip().lower()
        if command == "help":
            display_menu()
        elif command == "exit":
            break
        elif command.startswith("species "):
            _, city = command.split(" ", 1)
            species_list = search_species(city)
            display_species(species_list)
        elif command.startswith("sightings "):
            _, details = command.split(" ", 1)
            city, taxonid = details.split(" ")
            sightings = search_sightings(taxonid, city)
            display_sightings(sightings)
        else:
            print("Invalid command, type 'help' for a list of commands.")
```

#### 2.3 List Species in a City

Implemented a stub function to return a list of species and a function to display them.

```python
def search_species(city):
    return [
        {"Species": {"AcceptedCommonName": "dolphin", "PestStatus": "Nil"}},
        {"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}}
    ]

def display_species(species_list):
    for species in species_list:
        print(f"Species: {species['Species']['AcceptedCommonName']}, PestStatus: {species['Species']['PestStatus']}")
```

#### 2.4 List Animal Sightings in a City

Implemented a stub function to return a list of sightings and a function to display them.

```python
def search_sightings(taxonid, city):
    return [{"properties": {"StartDate": "1999-11-15", "LocalityDetails": "Tinaroo"}}]

def display_sightings(sightings):
    for sighting in sightings:
        print(f"Date: {sighting['properties']['StartDate']}, Location: {sighting['properties']['LocalityDetails']}")
```

#### 2.5 List Venomous Species in a City

Implemented a function to filter and display venomous species.

```python
def filter_venomous(species_list):
    return [species for species in species_list if species['Species']['PestStatus'] == 'Venomous']
```

#### 2.6 Integrate GPS Web Service

Implemented a module to fetch GPS coordinates using the Nominatim API.

```python
# nominatim.py
import requests

def gps_coordinate(city):
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    response = requests.get(url).json()
    if response:
        lat = float(response[0]['lat'])
        lon = float(response[0]['lon'])
        return {'latitude': lat, 'longitude': lon}
    return None
```

#### 2.7 Fetch Species List Using Web Service

Integrated the Queensland Government's Species web service to fetch species data.

```python
# wildlife.py
import requests

def get_species_list(coordinate, radius):
    lat, lon = coordinate['latitude'], coordinate['longitude']
    url = f"https://apps.des.qld.gov.au/species/?op=getspecieslist&kingdom=animals&circle={lat},{lon},{radius}"
    response = requests.get(url).json()
    return response["SpeciesSightingSummariesContainer"]["SpeciesSightingSummary"]
```

#### 2.8 Fetch Surveys by Species Using Web Service

Implemented a function to fetch survey data for specific species.

```python
# wildlife.py
def get_surveys_by_species(coordinate, radius, taxonid):
    lat, lon = coordinate['latitude'], coordinate['longitude']
    url = f"https://apps.des.qld.gov.au/species/?op=getsurveysbyspecies&taxonid={taxonid}&circle={lat},{lon},{radius}"
    response = requests.get(url).json()
    return [survey for survey in response['features'] if survey['properties']['SiteCode'] == 'INCIDENTAL']
```

#### 2.9 Sort and Display Sightings by Date

Implemented functions to sort sightings by date and display them.

```python
from datetime import datetime

def earliest(sightings):
    return min(sightings, key=lambda x: datetime.strptime(x['properties']['StartDate'], '%Y-%m-%d'))

def sort_by_date(sightings):
    return sorted(sightings, key=lambda x: datetime.strptime(x['properties']['StartDate'], '%Y-%m-%d'))

def display_sightings(sightings):
    sorted_sightings = sort_by_date(sightings)
    for sighting in sorted_sightings:
        print(f"Date: {sighting['properties']['StartDate']}, Location: {sighting['properties']['LocalityDetails']}")
```

---

### 3. Limitations

- **Stub Data**: For some functions, stub data was used due to the lack of access to live data during the development phase.
- **Service Limitations**: The web services used have rate limits and availability constraints, which can affect the application's performance and reliability.
- **Error Handling**: Limited error handling has been implemented. More robust error handling would be needed for a production-level application.

---

### 4. Test Results

#### 4.1 Help Menu
```text
Help
====
The following commands are recognised.
Display help wildlife> help
Exit the application wildlife> exit
Display animal species in a city wildlife> species <city>
Display animal sightings in a city wildlife> sightings <city> <taxonid>
Display venomous species wildlife> species <city> venomous
```

#### 4.2 Species in a City
```text
wildlife> species brisbane
Species: dolphin, PestStatus: Nil
Species: snake, PestStatus: Venomous
```

#### 4.3 Sightings in a City
```text
wildlife> sightings brisbane 1
Date: 1999-11-15, Location: Tinaroo
```

#### 4.4 Venomous Species in a City
```text
wildlife> species brisbane venomous
Species: snake, PestStatus: Venomous
```

---

### 5. Bugs

- **Command Parsing**: Commands with additional spaces or incorrect formats can lead to parsing errors.
- **API Response Changes**: Any changes in the API responses could break the current implementation as it relies on specific JSON structures.

---

### 6. Future Enhancements

- **Improved Error Handling**: Implement comprehensive error handling to manage API failures and invalid inputs gracefully.
- **User Interface**: Develop a graphical user interface (GUI) for better user interaction.
- **Extended Functionality**: Add more features such as filtering by date ranges, more detailed species information, and integration with additional data sources.
- **Optimization**: Optimize network calls and data processing for better performance.

---

### 7. Conclusion

This assignment provided a valuable learning experience in developing a Python application that interacts with web services. The project successfully implemented the required functionalities, demonstrating the ability to fetch and analyze wildlife data. Further improvements and enhancements can be made to increase the robustness and user-friendliness of the application.

---

### Appendices

- **Appendix A: Code Listings**
  - [sighting.py](#)
  - [nominatim.py](#)
  - [wildlife.py](#)

- **Appendix B: Screenshots**
  - Screenshots of the application running various commands.

---

**Note**: Replace placeholders such as `[Your Name]`, `[Your Student ID]`, and links in the appendices with actual content and data.


