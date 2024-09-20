import pandas as pd
import re

def load_data(filepath):
  try:
    return pd.read_csv(filepath)
  except FileNotFoundError as e:
    print(f"Error: File Not Found. {e}")
    # can be our file error number
    # if 69 do stuff etc 
    return 69

def search_function(keyword, tableData):
    # returns boolean series of matches ignores casing
    loc = [bool(re.search(keyword, name, re.IGNORECASE)) for name in tableData["food"]]
    # returns new dataframe with only matches, and the number of results
    return tableData[loc], sum(loc)


def num_of_rows(num):
  return f"Number Of Results: {str(num)}"
