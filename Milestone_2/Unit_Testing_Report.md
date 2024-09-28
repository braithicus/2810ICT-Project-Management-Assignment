# Unit Testing Report

Please provide your GitHub repository link.

### GitHub Repository URL: https://github.com/braithicus/2810ICT-Project-Management-Assignment

---

The testing report should focus solely on <span style="color:red"> testing all the self-defined functions related to
the five required features.</span> There is no need to test the GUI components. Therefore, it is essential to decouple your code and separate the logic from the GUI-related code.

## 1. **Test Summary**

list all tested functions related to the five required features and the corresponding test functions designed to test
those functions, for example:

| **Tested Functions**                                                    | **Test Functions**                                                                 |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `load_data(filepath)`                                                   | `test_load_data_valid()` <br> `test_load_data_invalid()`                           |
| `search_function(keyword, dFrame)`                                      | `test_search_function_valid()` <br> `test_search_function_invalid()`               |
| `num_of_rows(num)`                                                      | `test_num_of_rows()`                                                               |
| `nutrition_range_filter(dFrame, nutrientName, minVal=0, maxVal=np.inf)` | `test_nutrition_range_filter_valid()` <br> `test_nutrition_range_filter_invalid()` |
| `nutrition_level_filter(dFrame, nutrientName, level=None)`              | `test_nutrition_level_filter_valid()` <br> `test_nutrition_level_filter_invalid()` |

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
df = af.load_data('sample_data.csv')

def test_load_data_valid():
  test_data = pd.DataFrame({
  'food': ["Peanut Butter", "Apple Pie", "Another Random Item", "Butter Scotch"],
  'Poison': [345, 987, 531, 7],
  'Row Number': [1, 2, 3, 4]
  })

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
   -  `test_divide_valid()`
   -  `test_divide_invalid()`
-  **Tested Function/Module**
   -  `divide(a, b)`
-  **Description**
   -  A brief description of the tested function's usage, including its purpose, input, and output.
-  **1) Valid Input and Expected Output**

| **Valid Input**               | **Expected Output** |
| ----------------------------- | ------------------- |
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

-  **1) Code for the Test Function**

```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```

-  **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
| ----------------------------- | ------------------- |
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

-  **2) Code for the Test Function**

```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```

### Test Case 3:

-  **Test Function/Module**
   -  `test_divide_valid()`
   -  `test_divide_invalid()`
-  **Tested Function/Module**
   -  `divide(a, b)`
-  **Description**
   -  A brief description of the tested function's usage, including its purpose, input, and output.
-  **1) Valid Input and Expected Output**

| **Valid Input**               | **Expected Output** |
| ----------------------------- | ------------------- |
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

-  **1) Code for the Test Function**

```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```

-  **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
| ----------------------------- | ------------------- |
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

-  **2) Code for the Test Function**

```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```

### Test Case 4:

-  **Test Function/Module**
   -  `test_divide_valid()`
   -  `test_divide_invalid()`
-  **Tested Function/Module**
   -  `divide(a, b)`
-  **Description**
   -  A brief description of the tested function's usage, including its purpose, input, and output.
-  **1) Valid Input and Expected Output**

| **Valid Input**               | **Expected Output** |
| ----------------------------- | ------------------- |
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

-  **1) Code for the Test Function**

```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```

-  **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
| ----------------------------- | ------------------- |
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

-  **2) Code for the Test Function**

```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```

### Test Case 5:

-  **Test Function/Module**
   -  `test_divide_valid()`
   -  `test_divide_invalid()`
-  **Tested Function/Module**
   -  `divide(a, b)`
-  **Description**
   -  A brief description of the tested function's usage, including its purpose, input, and output.
-  **1) Valid Input and Expected Output**

| **Valid Input**               | **Expected Output** |
| ----------------------------- | ------------------- |
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

-  **1) Code for the Test Function**

```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```

-  **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
| ----------------------------- | ------------------- |
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

-  **2) Code for the Test Function**

```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```

### Test Case 6:

add more test cases if necessary.

## 3. **Testing Report Summary**

Include a screenshot of unit_test.html showing the results of all the above tests.

You can use the following command to run the unit tests and generate the unit_test.html report.

```commandline
pytest test_all_functions.py --html=unit_test.html --self-contained-html
```

Note: test_all_functions.py should contain all the test functions designed to test the self-defined functions related
to the five required features.

![unit_test_summary](./Unit_test.png)
