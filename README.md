# 3155-Project
Project 1 for ITSC-3155-002

### Note:
I tried to reach out to my teammates via e-mail and will try again tomorrow in-class but I have not heard from them. Coming to class has become a huge problem with changes in work and home life. Please let me know if there are any alternatives. I do not mind attempting the project on my own.

# Group Members

* [Samuel Edwards](mailto:sedwar92@uncc.edu)
* [Mekhi Washington](mmailto:mwashi35@uncc.edu)
* [Rohan Bharde](mmailto:rbharde@uncc.edu)
* [Josh Prince](mmailto:jprinc16@uncc.edu)

# Revisions

|  Version  |  Date  |  Description  |  Author  |  Reviewed By  |

| 1.0 | 03/22/23 | Initial draft | [Samuel Edwards](mailto:sedwar92@uncc.edu) | [Samuel Edwards](mailto:sedwar92@uncc.edu) |

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Constraints](#constraints)
4. [Use Cases](#use-cases)
5. [User Stories](#user-stories)
6. [Glossary](#glossary)

# **Introduction**
This program will act as a platform for a user to scrape Expedia for flight information. It will utilize a GUI for ease of use in conjunction with a terminal prompt that will allow the user to sort and choose flights. It will use a SQL(or .csv) backend for storing the flight information that will be sorted and displayed. It will then be able to complete the booking process if the user has provided the correct credentials.

# **Requirements**

## Group Member 1:
### REQ-1
**Description:** Scrape travel options from Expedia. (Booking platform may change depending on how complex the API is)  
**Type:** Functional  
**Priority:** 1  
**Testing:** Verify successful data scraping.  

### REQ-2
**Description:** Store and retrieve data using an SQL database.  
**Type:** Functional  
**Priority:** 1  
**Testing:** Test data storage and retrieval.  

### REQ-3
**Description:** Ability to save the flight search as a template for future use.  
**Type:** Functional  
**Priority:** 4  
**Testing:** Check to see if user can save, then load the template.  

## Group Member 2:

### REQ-4
**Description:** Allow booking of flight. (Maybe see if program can go all the way to confirmation page or payment page using a 000000 credit card number.)  
**Type:** Functional  
**Priority:** 1  
**Testing:** Test booking process.  

### REQ-5
**Description:** Gives a list of flights that the user can choose from. (in terminal)  
**Type:** Functional  
**Priority:** 1  
**Testing:** Verify list is easily read and formatted well.  

### REQ-6
**Description:** Gives sorting ability to list of flights. (get list of commands the user can use)  
**Type:** Functional  
**Priority:** 3  
**Testing:** Verify sorting is happening correctly.  

## Group Member 3:

### REQ-7
**Description:** Create a GUI that the user can use to book. (Dropdown menu for carrier preference)  
**Type:** Functional  
**Priority:** 1  
**Testing:** Conduct tests that make sure drop-down menus and inputs work.  

### REQ-8
**Description:** Provide tooltips and help documentation (a pdf guide).  
**Type:** Functional  
**Priority:** 3  
**Testing:** Check that tooltips appear when hovered over GUI items.  

### REQ-9
**Description:** Implement a login system. (Can try encryption with hashing from previous lab)  
**Type:** Functional  
**Priority:** 3  
**Testing:** Test login and encryption.  

## Group Member 4:

### REQ-10
**Description:** Enable itinerary printing via PDF. (or notepad depending on how complicated PDF output is)  
**Type:** Functional  
**Priority:** 4  
**Testing:** Verify functionality by making sure the output is legible and formatted correctly.  
### REQ-11
**Description:** Add calendar to the GUI for easier date selection for booking.  
**Type:** Functional  
**Priority:** 4  
**Testing:** Verify functionality by making sure the output is legible and formatted correctly.  
### REQ-12
TBD  
