import all_functions as af
import pandas as pd

def test_load_data():
  # making a small dataframe for testing
  test_data = pd.DataFrame({
  'food': ["Peanut Butter", "Apple Pie", "Another Random Item", "Butter Scotch"],
  'Poison': [345, 987654, 8765, 7],
  'Row Number': [1, 2, 3, 4]
  })

  # calling the load data function on a csv with the same data as the test dataframe
  loaded_data = af.load_data('sample_data.csv')

  # assert that the function returns the same result as the test dataframe
  pd.testing.assert_frame_equal(loaded_data, test_data)

  # assert the fail returns 69
  no_file = af.load_data('non-existent-file.csv')
  assert no_file == 1


def test_search_function():
  # same test dataframe as before
  df = af.load_data('sample_data.csv')

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
  'Poison': [345, 987654, 8765, 7],
  'Row Number': [1, 2, 3, 4]
  })
  pd.testing.assert_frame_equal(result2, expected_result2)
  assert row_num2 == 4

  # search for something that does not exist (no results)
  result3, row_num3 = af.search_function('Does Not Exist', df)
  expected_result3 = pd.DataFrame({
  'food': pd.Series([], dtype='object'),
  'Poison': pd.Series([], dtype='int64'),
  'Row Number': pd.Series([], dtype='int64')
  })
  pd.testing.assert_frame_equal(result3, expected_result3)
  assert row_num3 == 0


def test_num_of_row():
  assert af.num_of_rows(5) == "Number Of Results: 5"
  assert af.num_of_rows(0) == "Number Of Results: 0"
  assert af.num_of_rows(10) == "Number Of Results: 10"

def test_nutrition_range_filter():
  df = af.load_data('sample_data.csv')

  result = af.nutrition_range_filter(df, 'Poison', minVal=-9999999, maxVal=9999999)
  expected_result = pd.DataFrame({
  'food': ["Peanut Butter", "Apple Pie", "Another Random Item", "Butter Scotch"],
  'Poison': [345, 987654, 8765, 7],
  'Row Number': [1, 2, 3, 4]
  })
  pd.testing.assert_frame_equal(result, expected_result)

  result2 = af.nutrition_range_filter(df, 'Poison')
  pd.testing.assert_frame_equal(result2, expected_result)

  result3 = af.nutrition_range_filter(df, 'Poison', minVal=300, maxVal=9000)
  expected_result3 = pd.DataFrame({
  'food': ["Peanut Butter", "Another Random Item"],
  'Poison': [345, 8765],
  'Row Number': [1, 3]
  }, index=[0, 2])
  pd.testing.assert_frame_equal(result3, expected_result3)

  result4 = af.nutrition_range_filter(df, 'Row Number', minVal=2, maxVal=4)
  expected_result4 = pd.DataFrame({
  'food': ["Apple Pie", "Another Random Item", "Butter Scotch"],
  'Poison': [987654, 8765, 7],
  'Row Number': [2, 3, 4]
  }, index=[1, 2, 3])
  pd.testing.assert_frame_equal(result4, expected_result4)

  result5 = af.nutrition_range_filter(df, 'Does Not Exist', minVal=300, maxVal=9000)
  assert result5 == 2