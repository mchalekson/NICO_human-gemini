import os
import re
import json
import pandas as pd

# === STEP 1: Extract speaker counts from JSON files ===
base_path = "/Users/maxchalekson/Projects/NICO-Research/NICO_human-gemini/gemini_data_analysis/data/"
conference_folders = ["2021MND", "2021ABI", "2021SLU", "2021MZT"]
participant_records = []

for conf in conference_folders:
    conf_path = os.path.join(base_path, conf)
    if not os.path.isdir(conf_path):
        print(f"Folder not found: {conf_path}")
        continue
    
    print(f"\n🔍 Searching folder: {conf_path}")
    for filename in os.listdir(conf_path):
        if filename.endswith(".json") and re.match(r"\d{4}_\d{2}_\d{2}_.+_S\d+\.json", filename):
            filepath = os.path.join(conf_path, filename)
            try:
                with open(filepath, "r") as f:
                    data = json.load(f)
                all_speakers = data.get("all_speakers", [])
                clean_speakers = [s for s in all_speakers if s and s.lower() != "none"]
                participant_records.append({
                    "conference": conf,
                    "session": filename.replace(".json", ""),
                    "n_participants": len(set(clean_speakers))
                })
            except Exception as e:
                print(f" Failed to process {filename}: {e}")

# Convert to DataFrame
df_participants = pd.DataFrame(participant_records)
print(f"\n Extracted participant counts for {len(df_participants)} sessions")

# === STEP 2: Merge with your existing Excel dataset ===
excel_path = "/Users/maxchalekson/Projects/NICO-Research/NICO_human-gemini/Data/updated_all_data_df.xlsx"
df_existing = pd.read_excel(excel_path)

# Merge based on 'session' column
df_merged = df_existing.merge(df_participants[["session", "n_participants"]], on="session", how="left")

# Save to new Excel file
output_path = "/Users/maxchalekson/Projects/NICO-Research/NICO_human-gemini/updated_all_data_with_participants.xlsx"
df_merged.to_excel(output_path, index=False)

print(f"\n Merged and saved updated file with participant counts to:\n{output_path}")