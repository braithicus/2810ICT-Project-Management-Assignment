# Project Plan

## Project Name: Comprehensive Food GUI

## Group Number: 023

### Team Members

| Student No. | Full Name             | GitHub Username      | Contribution (sum to 100%) |
| ----------- | --------------------- | -------------------- | -------------------------- |
| s5398289    | William-Joseph Simons | William-JosephSimons | 33.3% or Equal             |
| s5265839    | Ben Lange             | s5265839-Griffith    | 33.3% or Equal             |
| s5264208    | Braith Lee            | braithicus           | 33.3% or Equal             |

### Brief Description of Contribution

Please Describe what you have accomplished in this group project.

-  s5398289, William-Joseph Simons
   -  Accomplishments: Project Objectives, Stakeholders, Scope, Problem Background
-  s5265839, Ben Lange
   -  Accomplishments: Describe what you have completed or achieved
-  s5264208, Braith Lee
   -  Accomplishments: Describe what you have completed or achieved

<div style="page-break-after: always;"></div>

# Table of Contents

-  [Project Plan](#project-plan)
   -  [1. Project Overview](#1-project-overview)
      -  [1.1 Project Objectives](#11-project-objectives)
      -  [1.2 Project Stakeholders](#12-project-stakeholders)
      -  [1.3 Project Scope](#13-project-scope)
   -  [2. Work Breakdown Structure](#2-work-breakdown-structure)
   -  [3. Activity Definition Estimation](#3-activity-definition-estimation)
   -  [4. Gantt Chart](#4-gantt-chart)

<div style="page-break-after: always;"></div>

## 1. Project Overview

### 1.1 Project Objectives

-  Provide a tool that allows users assess the nutritional value of different foods.
-  Provide a tool that allows the consumer to search the food by name.
-  Provide a tool that allows users to filter the nutritional data according to particular ranges and levels of nutrients
-  Provide a graphical user interface to allow for the data to be interacted with.
-  Allow for a foods nutritional value to be shown visually, with tools such as pie charts and bar graphs.
-  **ADDITIONAL FEATURE NEEDS TO BE ADDED**

### 1.2 Project Stakeholders

#### Project Manager

-  <h5 style="display: inline;"> Description: </h5> In charge of managing the project in its entirety and acting as the communicator between all stakeholders, making sure its stays within and meets the requirements of the scope.
-  <h5 style="display: inline;"> Role: </h5> Acts as the main point for communication. Coordinates and integrates the processes of: Initiating, Planning, Executing, Monitoring and Controlling, and Closing. And facilitates decisions made within the core knowledge areas such as: Integration, Scope, Time, Cost, Quality, Human Resources, Communication, Risk, and Procurement. This is done through delegation, or personally by the project manager.

#### Data Analysts

-  <h5 style="display: inline;"> Description: </h5> Professionals in the scope of analysing and interpreting data to gain insights and meaning.
-  <h5 style="display: inline;"> Role: </h5> Create algorithms to evaluate the Nutritional_Food_Database.csv, and identify metrics and trends in the data that allow for different visual representations. While also removing any anomalies from the dataset, ensuring high quality data. They also use their findings to effectively communicate complex insights to other stakeholders.

#### Software Developers

-  <h5 style="display: inline;"> Description: </h5> People who are skilled in designing, implementing, and testing software applications.
-  <h5 style="display: inline;"> Role: </h5> Implement and document the tools and analytical insights from the data analysts, while ensuring they are of high quality and thoroughly tested. This means ensuring that these tools meet the necessary requirements while being free of bugs, and documenting the process for other stakeholders.

#### Nutritionists and Dietitians

-  <h5 style="display: inline;"> Description: </h5> Professionals that are involved with advising people on their health related goals and their nutritional intake.
-  <h5 style="display: inline;"> Role: </h5> They will use the application to search for specific nutrients and analyse the data to come to conclusions on what the patient should do.

#### Educational Institutions

-  <h5 style="display: inline;"> Description: </h5> Institutions that involve educating the population such as schools and universities. Specifically institutions that teach topics involved with vitamins and nutrients such as health science.
-  <h5 style="display: inline;"> Role: </h5> Institutions will use the application as a resource to teach students about nutrition, and use the visualisation tool as way to better engage the students.

#### Health Conscious Individuals

-  <h5 style="display: inline;"> Description: </h5> A subset of the general public that is conscious of their health and is interested in maintaining a healthy lifestyle and diet.
-  <h5 style="display: inline;"> Role: </h5> These people will use the application to search for nutritional information on the food they are eating to make more informed choices.

#### Researchers

-  <h5 style="display: inline;"> Description: </h5> People within academic institutions that study dietary and nutritional information; doing projects and conducting tests, searching for patterns and how different nutrients impact human health.
-  <h5 style="display: inline;"> Role: </h5> They will use the application for easily searching through nutritional data and for its visualisation tools, to aid research projects.

#### Food Manufacturers

-  <h5 style="display: inline;"> Description: </h5> Companies that are involved in the selling, marketing, or producing food.
-  <h5 style="display: inline;"> Role: </h5> Companies will use the application to become more aware of the relative sizes of different nutrients in their products and to better market the product to consumers based on its content.

### 1.3 Project Scope

#### Inclusions

##### Graphical User Interface

An interface that allows users to easily and graphically navigate the Nutritional_Food_Database.csv.  
It includes:

-  A food item search feature
-  Tools for visualisation, such as bar graphs and pie charts
-  Menus to perform different actions on the data

##### Food Search Feature

A search feature that allows users to search for food items by name and see all its available nutritional data.  
It includes:

-  A search bar where you can enter the name of a food
-  A display that contains the nutritional information available for that food, along with visualisations of the data.
-  An autocomplete feature that helps in finding the desired food

##### Nutrition Breakdown Feature

A feature that allows the user to see the nutritional breakdown of the food item they selected through pie charts and bar graphs.  
It includes:

-  Pie charts and bar graphs
-  An interactive component that allows the user to flip between the bar graphs and pie charts

##### Nutrition Range Filter Feature

Allows users to select a nutrient and gives them the ability to input maximum and minimum values, and displays to them a list of foods that fall within that range.  
It includes:

-  A range menu for choosing between different nutrients
-  Fields to enter the maximum and minimum values
-  A display afterwards that contains the list of foods

##### Nutrition Level Filter Feature

Allows users to filter foods by their nutritional content levels: low, mid, and high. The filter includes: fat, protein, carbohydrates, sugar, and nutritional density.
It includes:

-  Low: Less than 33% of the highest value
-  Mid: Between 33% and 66% of the highest value
-  High: Greater than 66% of the highest value
-  A filter menu for choosing the level of each nutrient
-  Fields below each nutrient
-  A display afterwards that will contain the list of foods

##### ADDITIONAL FEATURE

##### Documentation

Documentation of the software that describes how it works, and how its meant to be used.
It includes:

-  Describes how the code will operate (function definitions, data structures, etc.)
-  Descriptions of what the system will do
-  Descriptions on how the user is required to interact with the software

##### Quality Assurance

Testing and validating the software to make sure it fulfils the scope to a high standard and is free of bugs.  
It includes:

-  Bug tracking and fixing
-  Thorough testing of the code

#### Exclusions

##### Real-Time Data Integration

Using a dynamic data source that is up to date.
It excludes:

-  Real time data
-  Data that is dynamic and updates

##### Multi-Language Support

Support for languages other than english within the program.
It excludes:

-  A menu for switching languages
-  A translation tool for the GUI

##### User Authentication and Security Features

Tools that involve authenticating the user and other security.
It excludes:

-  Multi-factor authentication
-  Encryption of the data
-  A login screen

##### Customisation Options

A feature that allows the user to customise the appearance of the GUI.
It excludes:

-  Different themes
-  Extensions

##### Advanced Analytics

Features that include things such as advanced analytics beyond basic filtering, ranges, and charts.  
It excludes:

-  Machine learning
-  Data mining

#### Scope Management

##### Regular Reviews

Rounds of regular reviewing of everyone's work to ensure that it stays within the scope.
It includes:

-  Regular weekly meetings
-  Reports on progress and changes made
-  Communication around the necessary future changes to be made to the project

## 2. Work Breakdown Structure

Include the Work Breakdown Structure (WBS) for the entire project. WBS should be presented as a hierarchical diagram. Use the elements from the WBS to define activities in Section 3, and schedule these activities in the Gantt Chart in Section 4. Ensure all project activities are considered and included in the WBS.

![WBS](./WBS.jpg)

## 3. Activity Definition Estimation

Define the activities required for your project based on the WBS, and assign responsibilities to team members. Each activity should be numbered and correspond with your Gantt chart. Provide estimated durations for each activity to facilitate Gantt chart preparation.

| Activity #No | Activity Name | Brief Description | Duration | Responsible Team Members |
| ------------ | ------------- | ----------------- | -------- | ------------------------ |
| xxx          | xxx           | xxx               | xxx      | xxx \& yyy               |
| xxxx         | xxx           | xxx               | xxx      | All                      |
| xxxx         | xxx           | xxx               | xxx      | xxx                      |

## 4. Gantt Chart

You have to use the provided Gantt chart template.

Use the provided Gantt chart template to list all items from the Activity Definition along with relevant estimates
and scheduling. Ensure that the Gantt chart reflects the activity definitions from Section 3. Track actual start
times and durations. Besides including Gantt chart here, you should also submit your Gantt chart file separately.
![Gantt Chart](./Gantt_chart.png)
