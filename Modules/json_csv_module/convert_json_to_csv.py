import pandas as pd

try:
    # Read the JSON file into a pandas DataFrame
    with open('data.json', encoding='utf-8') as inputfile:
        df = pd.read_json(inputfile)
        print("JSON data successfully loaded into DataFrame.")

    # Write the DataFrame to a CSV file
    try:
        df.to_csv('data1.csv', encoding='utf-8', index=False)
        print("Conversion successful! 'data1.csv' created.")
    except Exception as e:
        print(f"Error during CSV creation: {e}")

except FileNotFoundError:
    print("Error: 'data.json' file not found. Please provide the correct path.")
except Exception as e:
    print(f"Error: {e}")
