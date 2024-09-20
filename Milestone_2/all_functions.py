import pandas as pd
import re
import matplotlib.pyplot as plt

def load_data(filepath):
  try:
    return pd.read_csv(filepath)
  except FileNotFoundError as e:
    print(f"Error: File Not Found. {e}")
    # can be our file error number
    # if 69 do stuff etc 
    return 69
  
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


def search_function(keyword, tableData):
    # returns boolean series of matches ignores casing
    loc = [bool(re.search(keyword, name, re.IGNORECASE)) for name in tableData["food"]]
    # returns new dataframe with only matches, and the number of results
    return tableData[loc], sum(loc)


def num_of_rows(num):
  return f"Number Of Results: {str(num)}"


def nutrition_breakdown(foodRow, type='Bar'):
  nutrients = []
  if type == 'Bar':
    nutrients
  elif type == 'Pie':
    nutrients