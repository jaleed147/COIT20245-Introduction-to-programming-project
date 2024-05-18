
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


