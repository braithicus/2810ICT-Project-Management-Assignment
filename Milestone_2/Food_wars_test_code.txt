import pandas as pd
import matplotlib.pyplot as plt

def food_wars_comparison(food_inputs, nutrient, df):
    # Filter out empty inputs and ensure at least two foods are provided
    food_inputs = [food for food in food_inputs if food]
    if len(food_inputs) < 2:
        raise ValueError("Please enter at least two foods to compare.")
    
    # Filter data for selected foods and nutrient
    df_filtered = df[df['food'].isin(food_inputs)]
    if nutrient not in df.columns:
        raise ValueError(f"Nutrient '{nutrient}' not found in data.")

    # Plotting the data
    plt.figure(figsize=(10, 6))
    plt.bar(df_filtered['food'], df_filtered[nutrient], color='skyblue')
    plt.xlabel('Food')
    plt.ylabel(nutrient)
    plt.title(f'Comparison of {nutrient} for Selected Foods')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return df_filtered


# Sample CSV data (assuming it's loaded into a DataFrame)
test_data = pd.DataFrame({
  'food': ["Peanut Butter", "Apple Pie", "Another Random Item", "Butter Scotch"],
  'Poison': [345, 987, 531, 7],
  'Row Number': [1, 2, 3, 4]
  })

# Create a sample DataFrame
sample_df = pd.DataFrame(test_data)

# Define food items and nutrient for comparison
food_inputs = ["Apple", "Banana", "Carrot"]
nutrient = "Protein"

# Run the food_wars_comparison function and display the filtered DataFrame
try:
    filtered_df = food_wars_comparison(food_inputs, nutrient, sample_df)
    print("Filtered DataFrame:")
    print(filtered_df)
except ValueError as e:
    print(f"Error: {e}")
