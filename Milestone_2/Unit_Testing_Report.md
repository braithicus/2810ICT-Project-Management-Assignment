# Unit Testing Report

Please provide your GitHub repository link.

### GitHub Repository URL: https://github.com/braithicus/2810ICT-Project-Management-Assignment

---

The testing report should focus solely on <span style="color:red"> testing all the self-defined functions related to
the five required features.</span> There is no need to test the GUI components. Therefore, it is essential to decouple your code and separate the logic from the GUI-related code.

## 1. **Test Summary**

list all tested functions related to the five required features and the corresponding test functions designed to test
those functions, for example:

| **Tested Functions**                                                    | **Test Functions**                                                                    |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `load_data(filepath)`                                                   | `test_load_data_valid()` <br> `test_load_data_invalid()`                              |
| `search_function(keyword, dFrame)`                                      | `test_search_function_valid()` <br> `test_search_function_invalid()`                  |
| `num_of_rows(num)`                                                      | `test_num_of_rows()`                                                                  |
| `nutrition_range_filter(dFrame, nutrientName, minVal=0, maxVal=np.inf)` | `test_nutrition_range_filter_valid()` <br> `test_nutrition_range_filter_invalid()`    |
| `nutrition_level_filter(dFrame, nutrientName, level=None)`              | `test_nutrition_level_filter_valid()` <br> `test_nutrition_level_filter_invalid()`    |
| `nutrition_breakdown(foodRow, type='Bar'/'Pie')`                        | `test_nutrition_breakdown_valid(mock_show)` <br> `test_nutrition_breakdown_invalid()` |
| `food_wars(food_inputs, nutrient, df)`                                  | `test_food_wars_valid(mock_show)` <br> `test_food_wars_invalid()`                     |

---

## 2. **Test Case Details**

### Test Case 1:

-  **Test Function/Module**
   -  `test_load_data_valid()`
   -  `test_load_data_invalid()`
-  **Tested Function/Module**
   -  `load_data_(filepath)`
-  **Description**

   -  This function provides the dataframe that allows us to operate on the data. It takes a filepath to a csv and returns a pandas dataframe that contains all the data in the csv. If the filepath is invalid, it raises a FileNotFoundError.

-  **1) Valid Input and Expected Output**

| **Valid Input**                | **Expected Output**                                                                                                                                        |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `load_data('sample_data.csv')` | `pd.DataFrame({'food': ["Peanut Butter", "Apple Pie", "Another Random Item", "Butter Scotch"], 'Poison': [345, 987, 531, 7], 'Row Number': [1, 2, 3, 4]})` |

-  **1) Code for the Test Function**

```python
# calling the load data function on a csv with the same data as the test dataframe
# this small test dataframe is used globally throughout most tests
df = af.load_data('sample_data.csv')

def test_load_data_valid():
  # making a small dataframe for testing
  test_data = pd.DataFrame({
  'food': ["Peanut Butter", "Apple Pie", "Another Random Item", "Butter Scotch"],
  'Poison': [345, 987, 531, 7],
  'Row Number': [1, 2, 3, 4]
  })

  # assert that the function returns the same result as the test dataframe
  pd.testing.assert_frame_equal(df, test_data)
```

-  **2) Invalid Input and Expected Output**

| **Invalid Input**                    | **Expected Output** |
| ------------------------------------ | ------------------- |
| `load_data('non-existent-file.csv')` | `FileNotFoundError` |

-  **2) Code for the Test Function**

```python
def test_load_data_invalid():
  with pytest.raises(FileNotFoundError):
    af.load_data('non-existent-file.csv')
```

### Test Case 2:

-  **Test Function/Module**
   -  `test_search_function_valid()`
   -  `test_search_function_invalid()`
-  **Tested Function/Module**
   -  `search_function(keyword, dFrame)`
-  **Description**

   -  This function takes a string 'keyword' to search for that food within the food column of the second input to the function: the dataframe, and it returns a tuple that contains a dataframe with the matching rows, and the amount of results found. The search result is case insensitive. An empty string for keyword returns the entire dataframe, and if there is no results for keyword it returns an empty dataframe.

-  **1) Valid Input and Expected Output**

| **Valid Input**                 | **Expected Output**                                                                                                                                            |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `search_function('Butter', df)` | `(pd.DataFrame({'food': ["Peanut Butter", "Butter Scotch"], 'Poison': [345, 7], 'Row Number': [1, 4]}, index=[0, 3]), 2)`                                      |
| `search_function('', df)`       | `(pd.DataFrame({'food': ["Peanut Butter","Apple Pie", "Another Random Item", "Butter Scotch"], 'Poison': [345, 987, 531, 7], 'Row Number': [1, 2, 3, 4]}), 4)` |

-  **1) Code for the Test Function**

```python
def test_search_function_valid():
  # search for butter (something with two results)
  result, row_num = af.search_function('Butter', df)
  expected_result = pd.DataFrame({
  'food': ["Peanut Butter", "Butter Scotch"],
  'Poison': [345, 7],
  'Row Number': [1, 4]
  }, index=[0, 3])
  pd.testing.assert_frame_equal(result, expected_result)
  assert row_num == 2

  # search for nothing (all results)
  result2, row_num2 = af.search_function('', df)
  expected_result2 = pd.DataFrame({
  'food': ["Peanut Butter","Apple Pie", "Another Random Item", "Butter Scotch"],
  'Poison': [345, 987, 531, 7],
  'Row Number': [1, 2, 3, 4]
  })
  pd.testing.assert_frame_equal(result2, expected_result2)
  assert row_num2 == 4
```

-  **2) Invalid Input and Expected Output**

| **Invalid Input**                       | **Expected Output**                                                                                                                              |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `search_function('Does Not Exist', df)` | `(pd.DataFrame({'food': pd.Series([], dtype='object'), 'Poison': pd.Series([], dtype='int64'), 'Row Number': pd.Series([], dtype='int64')}), 0)` |

-  **2) Code for the Test Function**

```python
def test_search_function_invalid():
  # search for something that does not exist (no results)
  result3, row_num3 = af.search_function('Does Not Exist', df)
  expected_result3 = pd.DataFrame({
  'food': pd.Series([], dtype='object'),
  'Poison': pd.Series([], dtype='int64'),
  'Row Number': pd.Series([], dtype='int64')
  })
  pd.testing.assert_frame_equal(result3, expected_result3)
  assert row_num3 == 0
```

### Test Case 3:

-  **Test Function/Module**
   -  `test_num_of_rows(num)`
-  **Tested Function/Module**
   -  `num_of_rows(num)`
-  **Description**

   -  This function takes a number and returns a string that displays the number in a nicer format. It is used when displaying the number of results returned from a feature in the gui.

-  **1) Valid Input and Expected Output**

| **Valid Input**   | **Expected Output**       |
| ----------------- | ------------------------- |
| `num_of_rows(5)`  | `"Number Of Results: 5"`  |
| `num_of_rows(0)`  | `"Number Of Results: 0"`  |
| `num_of_rows(10)` | `"Number Of Results: 10"` |

-  **1) Code for the Test Function**

```python
def test_num_of_rows():
  assert af.num_of_rows(5) == "Number Of Results: 5"
  assert af.num_of_rows(0) == "Number Of Results: 0"
  assert af.num_of_rows(10) == "Number Of Results: 10"
```

### Test Case 4:

-  **Test Function/Module**
   -  `test_nutrition_range_filter_valid()`
   -  `test_nutrition_range_filter_invalid()`
-  **Tested Function/Module**
   -  `nutrition_range_filter(dFrame, nutrientName, minVal=0, maxVal=np.inf)`
-  **Description**

   -  This function takes a dataframe and nutrient string which is a column in the dataframe, and optional float min and max values. If the min value isn't given, it defaults to 0 and if the max value isn't given, it defaults to positive infinity. This function returns a filtered dataframe that contains only the foods (the rows) that fall between the min and max values for that nutrient. If the column name does not exist, the function raises a KeyError.

-  **1) Valid Input and Expected Output**

| **Valid Input**                                           | **Expected Output**                                                                                                                                        |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `nutrition_range_filter(df, 'Poison', -9999999, 9999999)` | `pd.DataFrame({'food': ["Peanut Butter", "Apple Pie", "Another Random Item", "Butter Scotch"], 'Poison': [345, 987, 531, 7], 'Row Number': [1, 2, 3, 4]})` |
| `nutrition_range_filter(df, 'Poison')`                    | `pd.DataFrame({'food': ["Peanut Butter", "Apple Pie", "Another Random Item", "Butter Scotch"], 'Poison': [345, 987, 531, 7], 'Row Number': [1, 2, 3, 4]})` |
| `nutrition_range_filter(df, 'Poison', 300, 600)`          | `pd.DataFrame({'food': ["Peanut Butter", "Another Random Item"], 'Poison': [345, 531], 'Row Number': [1, 3]}, index=[0, 2])`                               |
| `nutrition_range_filter(df, 'Row Number', 2, 4)`          | `pd.DataFrame({'food': ["Apple Pie", "Another Random Item", "Butter Scotch"], 'Poison': [987, 531, 7], 'Row Number': [2, 3, 4]}, index=[1, 2, 3])`         |

-  **1) Code for the Test Function**

```python
def test_nutrition_range_filter_valid():
  # test for range with extreme values. Returns entire dataframe
  result = af.nutrition_range_filter(df, 'Poison', -9999999, 9999999)
  expected_result = pd.DataFrame({
  'food': ["Peanut Butter", "Apple Pie", "Another Random Item", "Butter Scotch"],
  'Poison': [345, 987, 531, 7],
  'Row Number': [1, 2, 3, 4]
  })
  pd.testing.assert_frame_equal(result, expected_result)

  # test for unspecified range. Returns entire dataframe
  result2 = af.nutrition_range_filter(df, 'Poison')
  pd.testing.assert_frame_equal(result2, expected_result)

  # test for valid range. Returns dataframe with values in range
  result3 = af.nutrition_range_filter(df, 'Poison', 300, 600)
  expected_result3 = pd.DataFrame({
  'food': ["Peanut Butter", "Another Random Item"],
  'Poison': [345, 531],
  'Row Number': [1, 3]
  }, index=[0, 2])
  pd.testing.assert_frame_equal(result3, expected_result3)

  # test for searching other columns
  result4 = af.nutrition_range_filter(df, 'Row Number', 2, 4)
  expected_result4 = pd.DataFrame({
  'food': ["Apple Pie", "Another Random Item", "Butter Scotch"],
  'Poison': [987, 531, 7],
  'Row Number': [2, 3, 4]
  }, index=[1, 2, 3])
  pd.testing.assert_frame_equal(result4, expected_result4)
```

-  **2) Invalid Input and Expected Output**

| **Invalid Input**                                        | **Expected Output** |
| -------------------------------------------------------- | ------------------- |
| `nutrition_range_filter(df, 'Does Not Exist', 300, 600)` | `KeyError`          |

-  **2) Code for the Test Function**

```python
def test_nutrition_range_filter_invalid():
  # test for invalid column name.
  with pytest.raises(KeyError):
    af.nutrition_range_filter(df, 'Does Not Exist', 300, 600)
```

### Test Case 5:

-  **Test Function/Module**
   -  `test_nutrition_level_filter_valid()`
   -  `test_nutrition_level_filter_invalid()`
-  **Tested Function/Module**
   -  `nutrition_level_filter(dFrame, nutrientName, level=None)`
-  **Description**

   -  This function takes a dataframe and a nutrient string which is a column in the dataframe, and a level for that nutrient (Low: Less than 33% of the highest value, Mid: Mid: Between 33% and 66% of the highest value, or High: Greater than 66% of the highest value). The function returns a filtered dataframe that contains only the foods (the rows) that fall into the level for that nutrient. If the column name does not exist, the function raises a KeyError. If no level is given, the function raises a TypeError. If an invalid level is given that is not Low, Mid, or High, the function raises a TypeError.

-  **1) Valid Input and Expected Output**

| **Valid Input**                                | **Expected Output**                                                                                                          |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `nutrition_level_filter(df, 'Poison', 'Low')`  | `pd.DataFrame({'food': ["Butter Scotch"], 'Poison': [7], 'Row Number': [4]}, index=[3])`                                     |
| `nutrition_level_filter(df, 'Poison', 'Mid')`  | `pd.DataFrame({'food': ["Peanut Butter", "Another Random Item"], 'Poison': [345, 531], 'Row Number': [1, 3]}, index=[0, 2])` |
| `nutrition_level_filter(df, 'Poison', 'High')` | `pd.DataFrame({'food': ["Apple Pie"], 'Poison': [987], 'Row Number': [2]}, index=[1])`                                       |

-  **1) Code for the Test Function**

```python
def test_nutrition_level_filter_valid():
  # test for low level
  low = af.nutrition_level_filter(df, 'Poison', 'Low')
  expected_low = pd.DataFrame({
  'food': ["Butter Scotch"],
  'Poison': [7],
  'Row Number': [4]
  }, index=[3])
  pd.testing.assert_frame_equal(low, expected_low)

  # test for mid level
  mid = af.nutrition_level_filter(df, 'Poison', 'Mid')
  expected_mid = pd.DataFrame({
  'food': ["Peanut Butter", "Another Random Item"],
  'Poison': [345, 531],
  'Row Number': [1, 3]
  }, index=[0, 2])
  pd.testing.assert_frame_equal(mid, expected_mid)

  # test for high level
  high = af.nutrition_level_filter(df, 'Poison', 'High')
  expected_high = pd.DataFrame({
  'food': ["Apple Pie"],
  'Poison': [987],
  'Row Number': [2]
  }, index=[1])
  pd.testing.assert_frame_equal(high, expected_high)
```

-  **2) Invalid Input and Expected Output**

| **Invalid Input**                                     | **Expected Output** |
| ----------------------------------------------------- | ------------------- |
| `nutrition_level_filter(df, 'Poison')`                | `TypeError`         |
| `nutrition_level_filter(df, 'Does Not Exist', 'Low')` | `KeyError`          |
| `nutrition_level_filter(df, 'Poison', 'Extreme')`     | `TypeError`         |

-  **2) Code for the Test Function**

```python
def test_nutrition_level_filter_invalid():
  # test for no level input
  with pytest.raises(TypeError):
    af.nutrition_level_filter(df, 'Poison')

  # test for invalid column
  with pytest.raises(KeyError):
    af.nutrition_level_filter(df, 'Does Not Exist', 'Low')

  # test for invalid level
  with pytest.raises(TypeError):
    af.nutrition_level_filter(df, 'Poison', 'Extreme')
```

### Test Case 6:

-  **Test Function/Module**
   -  `test_nutrition_breakdown_valid()`
   -  `test_nutrition_breakdown_invalid()`
-  **Tested Function/Module**
   -  `nutrition_breakdown(foodRow, type='Bar'/'Pie')`
-  **Description**

   -  This function takes a series from the main dataframe which is a single row of food, and has the option between inputting Bar or Pie which chooses the chart type to be generated. The function uses matplotlib.pyplot to visualize the entire nutritional composition of the food row by generating the chosen chart type. The chart type by default is Bar, but if the chart type entered is invalid it raises a TypeError. A valid call of the function returns the figure of the chart being generated. If the type is Bar, the figure generated is a bar chart, where each bar represents a different nutrient. The chart title is 'Nutritional Breakdown', the x-axis tile is 'Nutrients' with the labels being the names of the nutrients, and the y-axis title is 'Amount (mg) which shows the integers of the amount in milligrams. Each bar's height represents the amount of the specific nutrient. A legend is also shown, titled 'Nutrient Amounts' that contains the data for every nutrient in text format.

-  **1) Valid Input and Expected Output**

| **Valid Input**                                   | **Expected Output** |
| ------------------------------------------------- | ------------------- |
| `nutrition_breakdown(df.iloc[0, 1:], type='Bar')` | `plt.gcf()`         |
| `nutrition_breakdown(df.iloc[0, 1:], type='Pie')` | `plt.gcf()`         |

-  **1) Code for the Test Function**

```python
# mocking plt.show so it doesn't display the figure and break everything
@patch('matplotlib.pyplot.show')
def test_nutrition_breakdown_valid(mock_show):
    foodRow = df.iloc[0, 1:]
    figure = af.nutrition_breakdown(foodRow, 'Bar')
    mock_show.assert_called_once()

    # testing for all valid labels
    axes = plt.gca()
    assert axes.get_title() == 'Nutritional Breakdown'
    assert axes.get_xlabel() == 'Nutrients'
    assert axes.get_ylabel() == 'Amount (mg)'

    # testing that the amount of bars is valid
    assert len(axes.patches) == len(foodRow)

    # testing all bar heights are valid
    bar_heights = [patch.get_height() for patch in axes.patches]
    assert bar_heights == list(foodRow.values)

    # testing all column labels are valid
    x_tick_labels = [label.get_text() for label in axes.get_xticklabels()]
    assert x_tick_labels == list(foodRow.index)

    # testing legend is valid
    legend = axes.get_legend()
    assert legend.get_title().get_text() == 'Nutrient Amounts'

    plt.close(figure)
```

**Add Pie chart tests**

-  **2) Invalid Input and Expected Output**

| **Invalid Input**                                     | **Expected Output** |
| ----------------------------------------------------- | ------------------- |
| `nutrition_breakdown(foodRow, type='Does Not Exist')` | `TypeError`         |

-  **2) Code for the Test Function**

```python
def test_nutrition_breakdown_invalid():
    foodRow = df.iloc[0, 1:]

    # testing invalid chart type throws type error
    with pytest.raises(TypeError):
        af.nutrition_breakdown(foodRow, type='Does Not Exist')
```

**Add Pie Chart Tests**

### Test Case 7:

-  **Test Function/Module**
   -  `test_food_wars_valid(mock_show)`
   -  `test_food_wars_invalid()`
-  **Tested Function/Module**
   -  `food_wars(food_inputs, nutrient, df)`
-  **Description**

   -  This function takes a list of string food names to compare, ignoring any empty strings, a string nutrient name, and the dataframe to be filtered. The function gets the specified foods (rows) from the dataframe and returns them while also showing and generating a bar chart using matplotlib.pyplot. The chart compares their differing values in the nutrient column. A bar is created for each food input, and the bar heights correspond to the nutrient levels.The chart title is "Food Wars: The [nutrient] Battles". The the x-axis title is "Food", with the labels being the names of the specific food, and the y-axis title is "[nutrient] (mg)", which shows the integers of the nutrient in mg. The chart requires at least two foods in the list to work and generates a ValueError if that's not the case. If the nutrient name is not found in the dataframe it also raises a ValueError.

-  **1) Valid Input and Expected Output**

| **Valid Input**                                                                  | **Expected Output**                                                                                                                  |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `food_wars(['Peanut Butter', 'Apple Pie', 'Another Random Item'], 'Poison', df)` | `pd.DataFrame({'food': ["Peanut Butter", "Apple Pie", "Another Random Item"], 'Poison': [345, 987, 531], 'Row Number': [1, 2, 3] })` |
| `food_wars(['Peanut Butter', '', 'Apple Pie', ''], 'Poison', df)`                | `pd.DataFrame({'food': ["Peanut Butter", "Apple Pie"], 'Poison': [345, 987], 'Row Number': [1, 2] })`                                |

-  **1) Code for the Test Function**

```python
@patch('matplotlib.pyplot.show')
def test_food_wars_valid(mock_show):
    food_inputs = ['Peanut Butter', 'Apple Pie', 'Another Random Item']

    result = food_wars(food_inputs, 'Poison', df)
    mock_show.assert_called_once()

    # testing for all valid labels
    fig = plt.gcf()
    ax = fig.gca()
    assert ax.get_title() == 'Food Wars: The Poison Battles'
    assert ax.get_xlabel() == 'Food'
    assert ax.get_ylabel() == 'Poison (mg)'

    # test if result is correct
    assert len(result) == 3
    assert list(result['food']) == food_inputs

    # testing that the amount of bars is valid
    assert len(ax.patches) == len(food_inputs)

    # testing all bar heights are valid
    bar_heights = [patch.get_height() for patch in ax.patches]
    assert bar_heights == [345, 987, 531]

    # testing all column labels are valid
    x_tick_labels = [label.get_text() for label in ax.get_xticklabels()]
    assert x_tick_labels == food_inputs

    plt.close(fig)

    # testing with empty inputs
    food_inputs_empty = ['Peanut Butter', '', 'Apple Pie', '']
    emptyResult = food_wars(food_inputs_empty, 'Poison', df)
    assert len(emptyResult) == 2
    assert list(emptyResult['food']) == ['Peanut Butter', 'Apple Pie']
```

-  **2) Invalid Input and Expected Output**

| **Invalid Input**                                                 | **Expected Output** |
| ----------------------------------------------------------------- | ------------------- |
| `food_wars(['Peanut Butter'], 'Poison', df)`                      | `ValueError`        |
| `food_wars(['Peanut Butter', 'Apple Pie'], 'Does Not Exist', df)` | `ValueError`        |

-  **2) Code for the Test Function**

```python
def test_food_wars_invalid():
    # testing with less than two foods
    with pytest.raises(ValueError):
        food_wars(['Peanut Butter'], 'Poison', df)

    # testing with invalid nutrient
    with pytest.raises(ValueError):
        food_wars(['Peanut Butter', 'Apple Pie'], 'Does Not Exist', df)
```

## 3. **Testing Report Summary**

Include a screenshot of unit_test.html showing the results of all the above tests.

You can use the following command to run the unit tests and generate the unit_test.html report.

```commandline
pytest test_all_functions.py --html=unit_test.html --self-contained-html
```

Note: test_all_functions.py should contain all the test functions designed to test the self-defined functions related
to the five required features.

![unit_test_summary](./Unit_test.png)
