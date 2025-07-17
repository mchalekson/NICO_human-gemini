import os
import json
import pandas as pd

# Path to your Excel file
excel_path = "/Users/maxchalekson/Projects/NICO-Research/NICO_human-gemini/Data/all_data_df.xlsx"
df = pd.read_excel(excel_path)


# Root folder where JSON data is stored
data_root = "/Users/maxchalekson/Projects/NICO-Research/NICO_human-gemini/gemini_data_analysis-EV/data"

# Dictionary to store total speaking length per session
speaking_lengths = {}

# Loop through each conference folder
for conference in ["2021MND", "2021ABI", "2021SLU", "2021MZT"]:
    folder_path = os.path.join(data_root, conference)
    for fname in os.listdir(folder_path):
        if fname.endswith(".json"):
            session_id = fname.replace(".json", "")
            full_path = os.path.join(folder_path, fname)
            with open(full_path, "r") as f:
                data = json.load(f)  # This is a dictionary
                if isinstance(data, dict) and "total_speaking_length" in data:
                    speaking_lengths[session_id] = data["total_speaking_length"]
                else:
                    speaking_lengths[session_id] = None  # Or 0, depending on how you want to treat missing data

# Add new column to your Excel DataFrame
df["total_speaking_length"] = df["session"].map(speaking_lengths)

# Save the updated Excel file
output_path = "/Users/maxchalekson/Projects/NICO-Research/NICO_human-gemini/Data/updated_all_data_df.xlsx"
df.to_excel(output_path, index=False)

print(f"Done. Updated file saved to: {output_path}")