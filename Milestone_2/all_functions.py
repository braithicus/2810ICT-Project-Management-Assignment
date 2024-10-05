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


# get a row from the dataframe
def nutrition_breakdown(foodRow, type='Bar'):
  food_name = foodRow['food']
  nutrient_data = foodRow.drop(['food', 'Nutrition Density', 'Caloric Value'])
  caloric_value = foodRow['Caloric Value']
  nutrition_density = foodRow['Nutrition Density']
  nutrient_data = nutrient_data[nutrient_data > 0]
  colours = plt.cm.tab20(np.linspace(0, 1, len(nutrient_data)))

  if type == 'Bar':
    fig, ax = plt.subplots(figsize=(12, 8))

    bar_graph = ax.bar(nutrient_data.index, nutrient_data.values, color=colours)
    ax.set_xlabel('Nutrients')
    ax.set_ylabel('Amount (mg)')
    ax.set_title(f'Nutritional Breakdown For {food_name}')
    
    plt.xticks(rotation=45, ha='right', fontsize=7)
    
    legend_labels = [f"{nutrient}: {value:.2f} mg" for nutrient, value in zip(nutrient_data.index, nutrient_data.values)]
    labels = legend_labels + [f"Caloric Value: {caloric_value:.2f} kcal",
                              f"Nutrition Density: {nutrition_density:.2f}"]
    
    extra_patch1 = plt.Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)
    extra_patch2 = plt.Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)
    handles = list(bar_graph) + [extra_patch1, extra_patch2]
    
    ax.legend(handles, labels, title='Nutrient Amounts', fontsize=5, bbox_to_anchor=(1.05, 1), loc='upper left')
    
    plt.tight_layout()
    plt.show()
    return fig

  elif type == 'Pie':
    fig, ax = plt.subplots(figsize=(12, 8))

    ax.set_title(f'Nutritional Breakdown For {food_name}', fontsize=16, pad=20)

    wedges, _ = ax.pie(nutrient_data.values, startangle=90, colors=colours, wedgeprops={'linewidth': 0.5, 'edgecolor': 'white', 'antialiased': True})
    ax.axis('equal')

    legend_labels = [f"{nutrient}: {value:.2f} mg" for nutrient, value in zip(nutrient_data.index, nutrient_data.values)]
    labels = legend_labels + [f"Caloric Value: {caloric_value:.2f} kcal",
                              f"Nutrition Density: {nutrition_density:.2f}"]
    
    extra_patch1 = plt.Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)
    extra_patch2 = plt.Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)
    handles = list(wedges) + [extra_patch1, extra_patch2]
    
    ax.legend(handles, labels, title='Nutrient Amounts', loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=8, title_fontsize=10)
    
    plt.tight_layout()
    plt.show()
    return fig
  else:
    raise TypeError(f"Invalid Chart Type")


def nutrition_range_filter(dFrame, nutrientName, minVal=0, maxVal=np.inf):
  try:
    return dFrame[dFrame[nutrientName].between(minVal, maxVal)]
  except KeyError as e:
    raise KeyError(f"KeyError: {e} - The column does not exist") from e


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