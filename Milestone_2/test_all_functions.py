import all_functions as af
from all_functions_ben import food_wars
import pandas as pd
import pytest
import matplotlib.pyplot as plt
from unittest.mock import patch

# calling the load data function on a csv with the same data as the test dataframe
# this small test dataframe is used globally throughout most tests
df = af.load_data('sample_data.csv')

# used for breakdown testing
df_whole = af.load_data('Food_Nutrition_Dataset.csv')
foodRow = df_whole.iloc[0]

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

# mocking plt.show so it doesn't display the figure and break everything
@patch('matplotlib.pyplot.show')
def test_nutrition_breakdown_valid(mock_show):
    figure = af.nutrition_breakdown(foodRow, 'Bar')
    mock_show.assert_called_once()

    nutrient_data = foodRow.drop(['food', 'Nutrition Density', 'Caloric Value'])
    nutrient_data = nutrient_data[nutrient_data > 0]

    # testing for all valid labels
    axes = plt.gca()
    assert axes.get_title() == f'Nutritional Breakdown For {foodRow["food"]}'
    assert axes.get_xlabel() == 'Nutrients'
    assert axes.get_ylabel() == 'Amount (mg)'

    # testing that the amount of bars is valid
    assert len(axes.patches) == len(nutrient_data)

    # testing all bar heights are valid
    bar_heights = [patch.get_height() for patch in axes.patches]
    assert bar_heights == list(nutrient_data.values)

    # testing all column labels are valid
    x_tick_labels = [label.get_text() for label in axes.get_xticklabels()]
    assert x_tick_labels == list(nutrient_data.index)

    # testing legend is valid
    legend = axes.get_legend()
    assert legend.get_title().get_text() == 'Nutrient Amounts'

    caloric_value = foodRow['Caloric Value']
    nutrition_density = foodRow['Nutrition Density']
    legend_labels = [label.get_text() for label in legend.get_texts()]
    expected_labels = (
      [f"{nutrient}: {value:.2f} mg" 
      for nutrient, value in zip(nutrient_data.index, nutrient_data.values)] 
      + [f"Caloric Value: {caloric_value:.2f} kcal",
        f"Nutrition Density: {nutrition_density:.2f}"]
    )
    
    assert legend_labels == expected_labels

    plt.close(figure)


    mock_show.reset_mock()
    figure2 = af.nutrition_breakdown(foodRow, 'Pie')
    mock_show.assert_called_once()

    # Testing for all valid labels
    axes2 = plt.gca()
    assert axes2.get_title() == f'Nutritional Breakdown For {foodRow["food"]}'

    # Testing that the pie chart is created correctly
    assert len(axes2.patches) == len(nutrient_data)

    # Testing legend is valid
    legend2 = axes2.get_legend()
    assert legend2.get_title().get_text() == 'Nutrient Amounts'

    legend_labels2 = [label.get_text() for label in legend2.get_texts()]
    expected_labels2 = (
      [f"{nutrient}: {value:.2f} mg" 
      for nutrient, value in zip(nutrient_data.index, nutrient_data.values)] 
      + [f"Caloric Value: {caloric_value:.2f} kcal",
        f"Nutrition Density: {nutrition_density:.2f}"]
    )
    
    assert legend_labels2 == expected_labels2

    plt.close(figure2)


def test_nutrition_breakdown_invalid():
    # testing invalid chart type throws type error
    with pytest.raises(TypeError):
        af.nutrition_breakdown(foodRow, type='Does Not Exist')

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

def test_food_wars_invalid():
    # testing with less than two foods
    with pytest.raises(ValueError):
        food_wars(['Peanut Butter'], 'Poison', df)

    # testing with invalid nutrient
    with pytest.raises(ValueError):
        food_wars(['Peanut Butter', 'Apple Pie'], 'Does Not Exist', df)


def test_to_mg():
  # specific nutrients start in grams
  data = pd.DataFrame({
    'food': ['Berries', 'Banana', 'Mud'],
    'Poison (mg)': [0, 5, 10], 
    'Row Number': [1, 2, 3], 
    'Fat': [23, 45, 67],
    'Saturated Fats': [12, 34, 56],
    'Monounsaturated Fats': [45, 12, 23],
    'Polyunsaturated Fats': [67, 23, 45],
    'Carbohydrates': [89, 67, 12],
    'Sugars': [34, 45, 89],
    'Protein': [56, 78, 90],
    'Dietary Fiber': [23, 34, 45],
    'Water': [78, 12, 34]
})
  
  # convert specific foods to milligrams
  data2 = pd.DataFrame({
    'food': ['Berries', 'Banana', 'Mud'],
    'Poison (mg)': [0, 5, 10],
    'Row Number': [1, 2, 3],  
    'Fat': [23000, 45000, 67000], 
    'Saturated Fats': [12000, 34000, 56000], 
    'Monounsaturated Fats': [45000, 12000, 23000], 
    'Polyunsaturated Fats': [67000, 23000, 45000],  
    'Carbohydrates': [89000, 67000, 12000],  
    'Sugars': [34000, 45000, 89000],  
    'Protein': [56000, 78000, 90000], 
    'Dietary Fiber': [23000, 34000, 45000], 
    'Water': [78000, 12000, 34000] 
})

  # call function on original gram data
  af.to_mg(data)

  # they are now equal
  pd.testing.assert_frame_equal(data, data2)