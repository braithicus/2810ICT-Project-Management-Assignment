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

---

## 2. **Test Case Details**

### Test Case 1:

-  **Test Function/Module**
   -  `test_load_data_valid()`
   -  `test_load_data_invalid()`
-  **Tested Function/Module**
   -  `load_data_(filepath)`
-  **Description**
   -  This function provides the dataframe that allows us to operate on the data. It takes a filepath to a csv and returns a pandas dataframe that contains all the data in the csv. If the filepath is invalid, it prints an error and returns a 1. This allows us to know that the load data function failed.
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
   -  A brief description of the tested function's usage, including its purpose, input, and output.
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
   -  A brief description of the tested function's usage, including its purpose, input, and output.
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
   -  A brief description of the tested function's usage, including its purpose, input, and output.
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
   -  A brief description of the tested function's usage, including its purpose, input, and output.
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
   -  Brief description yada yada yada, cant be bothered to english right now
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

## 3. **Testing Report Summary**

Include a screenshot of unit_test.html showing the results of all the above tests.

You can use the following command to run the unit tests and generate the unit_test.html report.

```commandline
pytest test_all_functions.py --html=unit_test.html --self-contained-html
```

Note: test_all_functions.py should contain all the test functions designed to test the self-defined functions related
to the five required features.

![unit_test_summary](./Unit_test.png)
