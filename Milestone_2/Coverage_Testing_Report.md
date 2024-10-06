# Coverage Testing Report

### GitHub Repository URL: https://github.com/braithicus/2810ICT-Project-Management-Assignment

---

## 1. **Test Summary**

| **Tested Functions**                                                    |
| ----------------------------------------------------------------------- |
| `load_data(filepath)`                                                   |
| `search_function(keyword, dFrame)`                                      |
| `num_of_rows(num)`                                                      |
| `nutrition_range_filter(dFrame, nutrientName, minVal=0, maxVal=np.inf)` |
| `nutrition_level_filter(dFrame, nutrientName, level=None)`              |
| `nutrition_breakdown(foodRow, type='Bar'/'Pie')`                        |
| `food_wars(food_inputs, nutrient, df)`                                  |
| `to_mg()`                                                               |

---

## 2. **Statement Coverage Test**

### 2.1 Description

To achieve %100 statement coverage it is required that all the lines of code in each of the functions is run at least once through the test cases that were built.
For the:

-  **test_load_data_valid() and test_load_data_invalid():** They ensure that the return line of reading the csv is covered correctly by giving the function a valid filepath, while also testing an invalid file path which runs the exception line of the load_data function.
-  **test_search_function_valid() and test_search_function_invalid():** They ensure that every line of the search function is run. Those lines are the list comprehension and the return statement. It tests many input values ensuring no errors are raised, even for a column in the dataframe that does not exist. Therefore, it always runs every line in the search function.
-  **test_num_of_rows():** This function only has one line; the return statement. Which always outputs the argument formatted in a string. Therefore, the tests always ensure 100% statement coverage.
-  **test_nutrition_range_filter_valid() and test_nutrition_range_filter_invalid():** These functions ensure that every possible argument is input to run every line of code in the nutrition_range_filter function. There are only two statements; returning a dataframe successfully and raising an KeyError due to an invalid column. To ensure both of these were covered, many valid arguments were given, and to cover the exception, an invalid column name was tested.
-  **test_nutrition_level_filter_valid() and test_nutrition_level_filter_invalid():** These functions test each level (Low, Mid, and High) to ensure each valid return statement is run and also tests the percentage calculation statements are run, while also testing an invalid level to ensure that exception is run. An invalid column name is given to ensure that the KeyError statement is also run.
-  **test_nutrition_breakdown_valid(mock_show) and test_nutrition_breakdown_invalid():** These functions ensure that every line is run in both the Bar and Pie branch. First, the show method is mocked to ensure the figure isn't displayed during testing. Everything in the figures is tested on both the pie and bar charts. This ensures that every statement for both figures is covered. An invalid type of chart is tested to ensure that the TypeError exception is covered.
-  **test_food_wars_valid(mock_show) and test_food_wars_invalid():** These tests ensure every statement for both valid and invalid inputs is run for the food_wars function. These functions ensure that both statements for the check of valid inputs and exceptions are run. The tests then ensure everything on the figure is displayed correctly, meaning every statement for the styling of the figure was run. It also tests that the return statement for the filtered dataframe is run.
-  **test_to_mg():** This test ensures that the line in the to_mg function is run, converting the required columns to milligrams. It does this by comparing a dataframe in grams and a dataframe in milligrams, then running the function on the one in grams, to compare if they are equal.

### 2.2 Testing Results

![statement_coverage](./statement_coverage.png)

## 3. **Branch Coverage Test**

### 3.1 Description

To achieve %100 branch coverage it is required that every branch of code in each of the functions is run at least once through the test cases that were built.
Functions without multiple branches won't be described. \*See statement coverage
For the:

-  **test_load_data_valid() and test_load_data_invalid():** They ensure that both the valid and invalid branch is run by reading a valid filepath to a csv, while also testing an invalid file path which runs the exception branch of the load_data function.
-  **test_nutrition_range_filter_valid() and test_nutrition_range_filter_invalid():** These functions ensure that every possible argument is input to run every branch of code in the nutrition_range_filter function. There are only two branches; returning a dataframe successfully and raising an KeyError due to an invalid column. To ensure both of these were covered, many valid arguments were given, and to cover the exception, an invalid column name was tested.
-  **test_nutrition_level_filter_valid() and test_nutrition_level_filter_invalid():** These functions test each level (Low, Mid, and High) to ensure each branch is run, including the main, while also testing an invalid level to ensure that the exception branch is run. An invalid column name is given to ensure that the KeyError branch is also run.
-  **test_nutrition_breakdown_valid(mock_show) and test_nutrition_breakdown_invalid():** These functions ensure that the Bar, Pie, and invalid branch is run. Tests are run with valid inputs, displaying both the Bar type and Pie type. An invalid type of chart is also tested to ensure that the TypeError exception branch is covered.
-  **test_food_wars_valid(mock_show) and test_food_wars_invalid():** These tests ensure every branch for both valid and invalid inputs is run for the food_wars function. These functions ensure that both the main branch is run and the branches for invalid inputs. It was tested with a food list argument less than 2, which covers that exception branch. It was also tested with an invalid column name to ensure that branch was also run.

### 3.2 Testing Results

![statement_coverage](./branch_coverage.png)
