# Software Design Document

## Project Name: Comprehensive Food GUI

## Group Number: 023

## Team members

| Student Number | Name                  |
| -------------- | --------------------- |
| s5398289       | William-Joseph Simons |
| s5265839       | Benjamin Lange        |
| s333333        | Full name             |

<div style="page-break-after: always;"></div>

# Table of Contents

<!-- TOC -->

- [Software Design Document](#software-design-document)
  - [Project Name: Comprehensive Food GUI](#project-name-comprehensive-food-gui)
  - [Group Number: 023](#group-number-023)
  - [Team members](#team-members)
- [Table of Contents](#table-of-contents)
  - [1. System Vision](#1-system-vision)
    - [1.1 Problem Background](#11-problem-background)
        - [Data Input](#data-input)
        - [Data Output](#data-output)
        - [Target Users](#target-users)
          - [Nutritionists and Dietitians](#nutritionists-and-dietitians)
          - [Educational Institutions](#educational-institutions)
          - [Health Conscious Individuals](#health-conscious-individuals)
          - [Researchers](#researchers)
          - [Food Manufacturers](#food-manufacturers)
    - [1.2 System capabilities/overview](#12-system-capabilitiesoverview)
      - [System Functionality](#system-functionality)
      - [Features and Functionalities:](#features-and-functionalities)
        - [GUI](#gui)
        - [Food Search](#food-search)
        - [Nutrition Breakdown](#nutrition-breakdown)
        - [Nutrition Range Filter](#nutrition-range-filter)
        - [Nutrition Level Filter](#nutrition-level-filter)
        - [Food Wars](#food-wars)
    - [1.3 Benefit Analysis](#13-benefit-analysis)
        - [1. Informed Dietary Choices](#1-informed-dietary-choices)
        - [2. Efficient Nutritional Research](#2-efficient-nutritional-research)
        - [3. Enhances Dietitians and Nutritionists](#3-enhances-dietitians-and-nutritionists)
        - [4. Educational Resource](#4-educational-resource)
        - [5. Marketing](#5-marketing)
        - [6. Time and Effort Savings](#6-time-and-effort-savings)
        - [7. ADDITIONAL FEATURE BENEFIT](#7-additional-feature-benefit)
  - [2. Requirements](#2-requirements)
    - [2.1 User Requirements](#21-user-requirements)
    - [2.2 Software Requirements](#22-software-requirements)
    - [2.3 Use Case Diagram](#23-use-case-diagram)
    - [2.4 Use Cases](#24-use-cases)
  - [3. Software Design and System Components](#3-software-design-and-system-components)
    - [3.1 Software Design](#31-software-design)
    - [3.2 System Components](#32-system-components)
      - [3.2.1 Functions](#321-functions)
      - [3.2.2 Data Structures / Data Sources](#322-data-structures--data-sources)
      - [3.2.3 Detailed Design](#323-detailed-design)
  - [4. User Interface Design](#4-user-interface-design)
    - [4.1 Structural Design](#41-structural-design)
    - [4.2 Visual Design](#42-visual-design)

<div style="page-break-after: always;"></div>

## 1. System Vision

### 1.1 Problem Background

-  <h5 style="display: inline;"> Problem Identification: </h5> This application fills the need for an easy to use tool that makes it possible for people to search for, analyse, visualise, and evaluate nutritional data for a variety of foods. This is specifically targeted and most useful for people who want to perform nutritional research and make informed decisions, or potentially give dietary advice. The current issues that aries without the use of this tool is the difficulty in determining the nutritional value of foods. This leads to unnecessary difficulty when trying to make healthy lifestyle choices, and when trying to carry out nutritional related research or education.
-  <h5 style="display: inline;"> Dataset: </h5> The Nutritional_Food_Database.csv is being used. This is a static food dataset that contains information regarding the nutritional information on a variety of foods. Columns in the dataset include:
-  -  Food
   -  Caloric Value
   -  Fat
   -  Carbohydrates
   -  Sugar
   -  Protein
   -  Nutritional Density
   -  Many other metrics for nutrition

##### Data Input

-  Users will be entering the names of foods to search the dataset.
-  Users will be selecting specific foods to see visualisation tools on its nutritional content.
-  Users will be inputting minimum and maximum values for a nutrition to display foods that fall within that range.
-  Users will be inputting low, mid, and high levels for various nutrients to display a list of filtered food items that fall within those ranges.
-  **ADDITIONAL ITEM CONTAINS INPUT**
-  The users will be accessing the Nutritional_Food_Database.csv via their inputs above.

##### Data Output

-  Visualisation tools such as pie charts and bar graphs when a food item is searched or clicked from a display.
-  A list of foods after the user inputs minimum and maximum values from the range menu
-  A list of foods after the user inputs low, mid, and high values from the filter menu.
-  **ADDITIONAL ITEM CONTAINS OUTPUT**

##### Target Users

###### Nutritionists and Dietitians

-  Why: To search for specific nutrients and analyse the data to give informed advice.

###### Educational Institutions

-  Why: As a resource to teach students about nutrition, and use the visualisation tool as way to better engage students.

###### Health Conscious Individuals

-  Why: To search for nutritional information on the food they are eating to make more informed choices.

###### Researchers

-  Why: For easily searching through nutritional data and for its visualisation tools, to aid research projects.

###### Food Manufacturers

-  Why: To become more aware of the relative sizes of different nutrients in their products and to better market the product to consumers based on its content.

### 1.2 System capabilities/overview

#### System Functionality

-  Users of the system will be able to search, filter, and visualise nutritional data from the Nutritional_Food_Database.csv with a user-friendly graphical user interface. The main objective is to allow users to more easily gain access to nutritional data so that they can gain insight into the content of their food.

#### Features and Functionalities:

##### GUI

-  An interface that allows users to easily and graphically navigate the Nutritional_Food_Database.csv.
   -  Functionality:
      -  A food item search feature
      -  Tools for visualisation, such as bar graphs and pie charts
      -  Menus to perform different actions on the data

##### Food Search

-  A search feature that allows users to search for food items by name and see all its available nutritional data.
   -  Functionality:
      -  A search bar where you can enter the name of a food
      -  A display that contains the nutritional information available for that food, along with visualisations of the data.
      -  An autocomplete feature that helps in finding the desired food

##### Nutrition Breakdown

-  A feature that allows the user to see the nutritional breakdown of the food item they selected through pie charts and bar graphs.
   -  Functionality:
      -  Pie charts and bar graphs
      -  An interactive component that allows the user to flip between the bar graphs and pie charts

##### Nutrition Range Filter

-  Allows users to select a nutrient and gives them the ability to input maximum and minimum values, and displays to them a list of foods that fall within that range.
   -  Functionality:
      -  A range menu for choosing between different nutrients
      -  Fields to enter the maximum and minimum values
      -  A display afterwards that contains the list of foods

##### Nutrition Level Filter

-  Allows users to filter foods by their nutritional content levels: low, mid, and high. The filter includes: fat, protein, carbohydrates, sugar, and nutritional density.
   -  Functionality:
      -  Low: Less than 33% of the highest value
      -  Mid: Between 33% and 66% of the highest value
      -  High: Greater than 66% of the highest value
      -  A filter menu for choosing the level of each nutrient
      -  Fields below each nutrient
      -  A display afterwards that will contain the list of foods

##### Food Wars
- **Description** 
  - Functionality:
    - **Functions**


### 1.3 Benefit Analysis

##### 1. Informed Dietary Choices

-  Benefit: By having easy and quick access to comprehensive nutritional data, users can make more informed dietary decisions.
-  Example: A health conscious person navigates the Nutritional_Food_Database.csv using the GUI. They enter the food 'avocado' into the search feature, and the auto complete allows them to quickly locate the food. Upon making the selection, the application shows the user a nutritional breakdown of the nutrients in the avocado using pie charts and bar graphs. The person can then use this new knowledge to inform themselves on whether they should include avocados in their diet.

##### 2. Efficient Nutritional Research

-  Benefit: More comprehensive and efficient research can be conducted by researchers.
-  Example: In order to conduct research on the impact sugar has on the health of the consumer, a researcher could navigate to the nutrition range feature menu and input sugar. They would then input different minimum and maximum values to display lists of foods with varying levels of sugar. The researcher can then select foods from the list to see a more comprehensive breakdown of the nutrients they contain, utilising the visualisation tools to further analyse the relative content of sugar in the foods.

##### 3. Enhances Dietitians and Nutritionists

-  Benefit: Dietitians are able to give more individualised, precise, and accurate recommendations.
-  Example: If a client is required to cut back on fats, but needs to maintain high levels of nutritional density and protein, they can utilise the nutrition level filter. By navigating to the filter menu and choosing low for fat, high for protein, and high for nutritional density, while leaving the rest blank. The dietitian can use the displayed list to provide customised food recommendations.

##### 4. Educational Resource

-  Benefit: The tool can be used by educational institutions to educate people on nutrition and data analysis.
-  Example: The application can be used in a class by a nutrition professor to teach students how to analyse and visualise nutritional data. The professor can search for different foods using the food search feature, and then they can get a nutritional breakdown of the food with pie charts and bar graphs to increase the engagement and understanding from the students, enhancing their learning experience.

##### 5. Marketing

-  Benefit: Manufacturers of food can make more informed choices surrounding the marketing of food.
-  Example: A food manufacturer can examine the nutritional content of their food using the nutrition breakdown feature with the visualisation tools. After the analysing the food, they can pinpoint nutrients that are high within their product such as necessary vitamins and use that as a way to target consumers with their marketing. Manufacturers can also use the nutrition range and filter feature to target specific nutrients to market.

##### 6. Time and Effort Savings

-  Benefit: Having a central, user-friendly source of information that contains a plethora of nutritional information saves time and effort compared to searching many sources for the same information.
-  Example: Using the auto complete of the food search feature allows a user to quickly locate the necessary food item. They search for "chicken breast" and analyse its protein content. The user then uses the nutrition range filter to find food with comparable protein content. They can now make more informed dietary decisions quicker and with less effort.

##### 7. ADDITIONAL FEATURE BENEFIT

## 2. Requirements

### 2.1 User Requirements

Detail how users are expected to interact with or use the program. What functionalities must the system provide from the end-user perspective? This can include both narrative descriptions and a listing of user needs.

Note: Since no specific client or user is assigned, you may create a fictional user. Who do you envision using your software?

### 2.2 Software Requirements

Define the functionality the software will provide. This section should list requirements formally, often using the word "shall" to describe functionalities.

Example Functional Requirements:

-  R1.1 The program shall accept multiple file names as arguments from the command line.
-  R1.2 Each file name can be a simple file name or include the full path of the file with one or more levels.

-  etc …

### 2.3 Use Case Diagram

Provide a system-level Use Case Diagram illustrating all required features.

Example:  
![Use Case Diagram](./UCD.png)

### 2.4 Use Cases

Include at least 5 use cases, each corresponding to a specific function.

| Use Case ID    | xxx  |
| -------------- | ---- |
| Use Case Name  | xxxx |
| Actors         | xxxx |
| Description    | xxxx |
| Flow of Events | xxxx |
| Alternate Flow | xxxx |

## 3. Software Design and System Components

### 3.1 Software Design

Include a flowchart that illustrates how your software will operate.

Example:  
![Software Design](./software_design_flowchart.png)

### 3.2 System Components

#### 3.2.1 Functions

List all key functions within the software. For each function, provide:

-  <h5 style="display: inline;"> Description: </h5> When creating functions of the software it is neccessary to reflect on the purpose of the software. For this case we would want:
    
    - <h6 style="display: inline;"> Food Search Function: </h6> to create a system that allows the users to analyse all nutritional information for specific foods
    - <h6 style="display: inline;"> Nutrition Breakdown Function: </h6> breakdown the nutritional information for that specific food in the form of pie and bar graphs
    - <h6 style="display: inline;"> Nutrition Range Filter Function:  </h6> allow the user to select one nutrition and input minimum & maximum values, and the tools will display a list of foods that fall into those ranges 
    - <h6 style="display: inline;"> Nutrition Level Filter Function: </h6> allow the user to select ranges of low, medium and high for nutritional information such as fats, protein carbohydrates, sugar and nutritional density to compare the foods that fall within the ranges visually 
    - <h6 style="display: inline;"> Food Wars Function: </h6> allow the user to select 5 chosen foods and compare them aginst each other visually with pie charts or bar graphs based on a one selected nutritonal information 
  
-  <h5 style="display: inline;"> Input Parameters: </h5>
    
    - <h6 style="display: inline;"> Food Search Function: </h6> The input type would be string and be used to input the foods the user is wanting to look up such as "pear"
    - <h6 style="display: inline;"> Nutrition Breakdown Function: </h6> The input type would be boolean as to allow the user to pick between bar chart or pie graph "Graph: 'bar' "
    - <h6 style="display: inline;"> Nutrition Range Filter Function: </h6> The input would be a combination input of a string and float32 to allow the user to first input the nutritional information and then input the minimum and maximum values for that nutrtional information such as "fats, minimum: 0.5000, maximum: 3.1240"
    - <h6 style="display: inline;"> Nutrition Level Filter Function: </h6> The input would be a string that allows the users to select the nutrional information to filter using such as "protein" then another string that only accepts three options of "low", "medium", "high"
    - <h6 style="display: inline;"> Food Wars Function: </h6> The input would be a combination of a set 5 strings that allow the user to select 5 foods such as "cheese sticks" "pear" "apple" "hummus" "fried rice" then another string for the nutrional information such as "sugar" and finally a boolean which would allow the user to select either pie or bar graph such as "Graph: 'pie' "

-  <h5 style="display: inline;"> Return Value: </h5> Describe what the function returns.
   
    - <h6 style="display: inline;"> Food Search Function: </h6> Would display all the information returned for the selected food such as in a dictionary for the user to view. 
    - <h6 style="display: inline;"> Nutrition Breakdown Function: </h6> Would display all the information for the selected food's nurtitional information as a bar or pie graph.
    - <h6 style="display: inline;"> Nutrition Range Filter Function: </h6> Would display all the foods between the selected minimum and maximum of the selected nutrition as a dictionary going from the food closest to the maximum with its value to the food closest to the minimum.
    - <h6 style="display: inline;"> Nutrition Level Filter Function: </h6> Have the foods that fall within the chosen parameters of low, medium or high for the selected nutritional value as a dictionary which will display the foods from the highest nutritional values to the lowest with the names of the foods
    - <h6 style="display: inline;"> Food Wars Function: </h6> It would have the function return the 5 selected foods compared against the nutritional value selected in the form of a bar or pie chart

-  <h5 style="display: inline;"> Side Effects: </h5> Note any side effects, such as changes to global variables or data passed by reference.
  
    - **I Have No Idea For This SEction Delete IF Nothing Put Down**
    - <h6 style="display: inline;"> Food Search Function: </h6>
    - <h6 style="display: inline;"> Nutrition Breakdown Function: </h6> 
    - <h6 style="display: inline;"> Nutrition Range Filter Function:  </h6>
    - <h6 style="display: inline;"> Nutrition Level Filter Function: </h6>
    - <h6 style="display: inline;"> Food Wars Function: </h6>

#### 3.2.2 Data Structures / Data Sources

List all data structures or sources used in the software. For each, provide:

-  Type: Type of data structure (e.g., list, set, dictionary). Dictionaries, Arrays **COME UP WITH MORE IDEAS**
-  Usage: Describe where and how it is used.
-  Functions: List functions that utilize this structure.

#### 3.2.3 Detailed Design

Provide pseudocode or flowcharts for all functions listed in Section 3.2.1 that operate on data structures. For instance, include pseudocode or a flowchart for a custom searching function.

## 4. User Interface Design

### 4.1 Structural Design

Present a structural design, a hierarchy chart, showing the overall interface’s structure. Address:

-  Structure: How will the software be structured?
-  Information Grouping: How will information be organized?
-  Navigation: How will users navigate through the software?
-  Design Choices: Explain why these design choices were made.

Example:  
![Structural Design](./Structural_Design.png)

### 4.2 Visual Design

Include all wireframes or mock-ups of the interface. Provide a discussion, explanation, and justification for your design choices. Hand-drawn wireframes are acceptable.

-  Interface Components: Clearly label all components.
-  Screens/Menus: Provide wireframes for different screens, menus, and options.
-  Design Details: Focus on the layout and size of components; color and graphics are not required.

Example:  
![Visual Design](./visual_design.png)
