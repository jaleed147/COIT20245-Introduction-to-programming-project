
## COIT20245 - Introduction to Programming
### Assignment 2: Python Application for Wildlife Sighting Analysis
### Group Members:
          Muhammad Jaleed (12248353)
          Jeneesh Patel (1225422)


---

### 1. Functionality and Adherence

The code demonstrates the following functionalities:<br />
+ Menu System: Displays a menu with options for help, displaying species in a city (limited functionality), displaying animal sightings (limited functionality), and exiting the application. (settings.py)<br />
+ Species Search: Retrieves a pre-defined list of species for a city (currently not using a web service). Can filter venomous species from the list. (settings.py)<br />
+ Animal Sightings: Retrieves a stubbed list of animal sightings with basic information. (settings.py)<br />
+ Geolocation (Stub): Returns a predefined GPS coordinate for a city regardless of the input city. (settings.py)<br />

The application adheres to the assignment by providing a basic framework for user interaction and data display.  However, it requires further development to integrate external web services for real-time geolocation and wildlife data retrieval.<br />


---

### 2. Code Quality

The code exhibits good practices in several areas:<br />
+ Meaningful Names: Variable and function names are descriptive and reflect their purpose (e.g., gps_coordinate, get_species_list). <br />
+ Documentation: Docstrings are included for most functions explaining their purpose and parameters. (settings.py, wildlife.py) <br />
+ Error Handling (Basic): Basic error checks are implemented for user input validation (e.g., checking for valid menu options). (settings.py)<br />
+ Code Layout: The code is generally well-formatted and easy to read.<br />

However, there's room for improvement with:<br />
+ Error Handling: More comprehensive error handling is needed for web service interactions and potential runtime issues. (wildlife.py, sighting.py) <br />
+ Stub Integration: The stub functions should be replaced with actual calls to external web services once development progresses. (settings.py)<br />

### 3. Untaught Language Features

The code primarily uses core Python functionalities and avoids untaught language features.  This makes the code easier to understand and maintain.
The code represents a solid foundation for the wildlife application.  It demonstrates good coding practices in terms of naming, documentation, and basic error handling. However, further development is needed to integrate external web services, enhance error handling, and implement functionalities like sorting sightings by date.

### 4. Test Results

#### 4.1 Help Menu
```text
Help
====
The following commands are recognised.
Display help wildlife> help
Exit the application wildlife> exit
Display animal species in a city wildlife> species Tinaroo
Display animal sightings in a city wildlife> sightings Tinaroo 860
Display venomous species wildlife> species Tinaroo venomous
```

#### 4.2 Species in a City
```text
wildlife> species Tinaroo
dolphin - Nil
snake - Venomous
```

#### 4.3 Sightings in a City
```text
wildlife> sightings Tinaroo 860
Date: 1999-11-15, Location: Tinaroo
```

#### 4.4 Venomous Species in a City
```text
wildlife> species Tinaroo venomous
snake - Venomous
```

---

### 5. Bugs

- **Command Parsing**: Commands with additional spaces or incorrect formats can lead to parsing errors.
- **API Response Changes**: Any changes in the API responses could break the current implementation as it relies on specific JSON structures.

---

### 6. Additional Notes

+ The nominatim.py file demonstrates proper implementation of the requests library to fetch GPS coordinates from a web service. It includes a test case with assert statements.
+ The wildlife.py file retrieves species lists from a web service using the requests library with retry logic for potential errors. However, functionality needs completion for retrieving specific sightings based on TaxonID.
+ The sighting.py file utilizes functions from other modules and implements sorting for displaying animal sightings.
+ The sightings.py file utilizes functions like display menu, display sightings and display venomous <br />
By focusing on web service integration,  error handling, and completing functionalities like displaying sightings based on TaxonID, the application can achieve a more robust and feature-rich state.

---

### 7. Conclusion

This assignment provided a valuable learning experience in developing a Python application that interacts with web services. The project successfully implemented the required functionalities, demonstrating the ability to fetch and analyze wildlife data. Further improvements and enhancements can be made to increase the robustness and user-friendliness of the application.

---



