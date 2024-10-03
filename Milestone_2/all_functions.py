import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np

def load_data(filepath):
  try:
    return pd.read_csv(filepath)
  except FileNotFoundError as e:
    raise FileNotFoundError(f"Error: File Not Found. {e}") from e
  
def to_mg(frame):
  columns_in_g = [
    'Fat', 
    'Saturated Fats', 
    'Monounsaturated Fats', 
    'Polyunsaturated Fats', 
    'Carbohydrates', 
    'Sugars', 
    'Protein', 
    'Dietary Fiber', 
    'Water'
  ]

  # MODIFIES ORIGINAL FRAME
  # dataframe all in mg now
  frame[columns_in_g] *= 1000


def search_function(keyword, dFrame):
    # returns boolean series of matches ignores casing
    loc = [bool(re.search(str(keyword), name, re.IGNORECASE)) for name in dFrame["food"]]
    # returns new dataframe with only matches, and the number of results
    return dFrame[loc], sum(loc)


def num_of_rows(num):
  return f"Number Of Results: {str(num)}"


# TODO: Charts unreadable and hideous
# USE: result.iloc[0, 1:] to get a foodRow series that retains column names 
# (the above statement gets first foodRow from dataframe and skips the first column which is the food name)
def nutrition_breakdown(foodRow, type='Bar'):
  if type == 'Bar':
    bar_graph = plt.bar(foodRow.index, foodRow.values)
    plt.xlabel('Nutrients')
    plt.ylabel('Amount (mg)')
    plt.xticks(rotation=45, ha='right', fontsize=7)
    plt.tight_layout()
    plt.title('Nutritional Breakdown')
    legend_labels = [f"{nutrient}: {value:.2f} mg" for nutrient, value in zip(foodRow.index, foodRow.values)]
    plt.legend(bar_graph, legend_labels, title='Nutrient Amounts', fontsize=5)
    plt.show()
  elif type == 'Pie':
    plt.pie(foodRow.values, labels=foodRow.index, autopct='%1.1f%%', shadow=True)
    plt.axis('equal')
    plt.show()
  else:
    raise TypeError(f"Invalid Chart Type")

# we could pass this new dataframe back into the search feature with no keyword
# to output to the search space. Once the search space is implemented ofc
def nutrition_range_filter(dFrame, nutrientName, minVal=0, maxVal=np.inf):
  try:
    return dFrame[dFrame[nutrientName].between(minVal, maxVal)]
  except KeyError as e:
    raise KeyError(f"KeyError: {e} - The column does not exist") from e

# same idea as range feature
def nutrition_level_filter(dFrame, nutrientName, level=None):
  try:
    nutrientColumn = dFrame[nutrientName]
  except KeyError as e:
    raise KeyError(f"KeyError: {e} - The column does not exist") from e
  
  maxVal = nutrientColumn.max()
  lowPercent, highPercent = maxVal * (33 / 100), maxVal * (66 / 100)
  if level == 'Low':
    return dFrame[nutrientColumn < lowPercent]
  elif level == 'Mid':
    return dFrame[nutrientColumn.between(lowPercent, highPercent)]
  elif level == 'High':
    return dFrame[nutrientColumn > highPercent]
  else:
    raise TypeError("Invalid Level")
  

df = load_data("Food_Nutrition_Dataset.csv")
to_mg(df)
result = df.iloc[0, 1:]
nutrition_breakdown(result, type='Bar')
