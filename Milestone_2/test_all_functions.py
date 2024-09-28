import all_functions as af
import pandas as pd
import pytest

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


def test_load_data_invalid():
  # assert the fail returns file not found error
  with pytest.raises(FileNotFoundError):   
    af.load_data('non-existent-file.csv')


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


def test_num_of_rows():
  assert af.num_of_rows(5) == "Number Of Results: 5"
  assert af.num_of_rows(0) == "Number Of Results: 0"
  assert af.num_of_rows(10) == "Number Of Results: 10"


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


def test_nutrition_range_filter_invalid():
  # test for invalid column name. 
  with pytest.raises(KeyError):
    af.nutrition_range_filter(df, 'Does Not Exist', 300, 600)


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